N = int(input())
A = list(map(int, input().split()))
subs = [[] for _ in range(N)]
for i, a in enumerate(A):
    subs[a - 1].append(i)

for i in range(N):
    print(len(subs[i]))