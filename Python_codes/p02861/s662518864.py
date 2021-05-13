from itertools import permutations
N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
r = []
for pp in permutations(P):
    t = 0
    for i in range(1, N):
        t += ((pp[i][0]-pp[i-1][0])**2 + (pp[i][1]-pp[i-1][1])**2)**(0.5)
    r.append(t)
print(sum(r)/len(r))
