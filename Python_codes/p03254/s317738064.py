# A - Candy Distribution Again
N,x = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = 0
for a in A:
    x -= a
    if x<0 or (ans==N-1 and x!=0):
        break
    ans += 1
print(ans)