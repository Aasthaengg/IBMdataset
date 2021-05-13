N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
D = [a-b for a,b in zip(A,B)]
D.sort()

lack = sum(d for d in D if d<0)

ans = 0
for d in D[::-1]:
    if lack < 0 and d > 0:
        ans += 1
        lack += d
    if d < 0:
        ans += 1
print(-1 if lack < 0 else ans)