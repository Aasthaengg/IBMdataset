N, K, Q = map(int, input().split())
p = [0]*N
for _ in range(Q):
    #p = list(map(lambda x : x-1, p))
    A = int(input())
    p[A-1] += 1

for ans in p:
    if ans <= Q-K:
        print("No")
    else:
        print("Yes")