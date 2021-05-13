N = int(input())
a = list(map(int, input().split()))
L = [[] for _ in range(N)]
for i in range(N):
    L[a[i]-1].append(i)
cnt = 0
for i in range(N):
    if a[i]-1 in L[i]:
        cnt += 1
print(cnt//2)