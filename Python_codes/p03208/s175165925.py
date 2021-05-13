N, K = map(int, input().split())
l=[]

for i in range(N):
    num = int(input())
    l.append(num)

ans = max(l) - min(l)
l.sort()

for i in range(N-K+1):
    a = l[i+K-1] - l[i]
    if a < ans:
        ans = a

print(ans)
