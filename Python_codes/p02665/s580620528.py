N = int(input())
A = list(map(int,input().split()))

if N == 0:
    print(1 if A[0] == 1 else -1)
    exit()

nodeS = [0 for i in range(N+1)]
nodeS[0] = 1
laS = [0 for i in range(N+1)]
laS[-1] = A[-1]

for i in range(N):
    laS[-2-i] = A[-2-i] + laS[-1-i]
    nodeS[i+1] = (nodeS[i]-A[i])*2

for i in range(N+1):
    if nodeS[i] <= 0:
        print(-1)
        exit()

for i in range(N+1):
    if nodeS[i] >= laS[i]:
        break
    if i == N:
        print(-1)
        exit()

print(sum(nodeS[:i]) + sum(laS[i:]))
