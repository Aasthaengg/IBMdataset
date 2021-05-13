# A - Candy Distribution Again
N,x = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
tmp = 0
ans = 0
for a in A:
    tmp += a
    if tmp<=x:
        ans += 1
    else:
        break
if ans==N and tmp!=x:
    ans -= 1
print(ans)