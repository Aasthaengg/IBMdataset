import math

class doubling:
    def __init__(self, seni, max_jump, reward = None):
        self.depth = math.ceil(math.log2(max_jump))
        self.N = len(seni)
        self.jumps = [[0 for i in range(self.N)] for _ in range(self.depth+1)]
        self.jumps[0] = seni
        
        if reward:
            self.rewards = [[0 for i in range(self.N)] for _ in range(self.depth+1)]
            self.rewards[0] = reward
            
        for i in range(self.depth):
            for j in range(self.N):
                self.jumps[i+1][j] = self.jumps[i][self.jumps[i][j]]
                if reward:
                    self.rewards[i+1][j] = self.rewards[i][j] + self.rewards[i][self.jumps[i][j]]
    def calculation(self, now, move):
        count = move.bit_length()
        reward = 0
        for i in range(count):
            if move & 1<<i == 1<<i:
                if self.rewards:
                    reward += self.rewards[i][now]
                now = self.jumps[i][now]
        return now, reward
#%%

N, K = map(int, input().split())
P = list(map(lambda x: int(x)-1, input().split()))
C = list(map(int, input().split()))
#%%

answer = -int(1e+50)

if K < N:
    minimum = K
else:
    minimum = N

for i in range(N):
    now2, reward2 = i, 0
    for j in range(minimum):
        reward2 = reward2 + C[now2]
        now2 = P[now2]
        if reward2 > answer:
            answer = reward2

consume = K-N
if consume > 0:
    dbl = doubling(P, consume, C)
    for i in range(N):
        now1, reward1 = dbl.calculation(i, consume)
        for j in range(N):
            reward1 = reward1 + C[now1]
            now1 = P[now1]
            if reward1 > answer:
                answer = reward1
print(answer)