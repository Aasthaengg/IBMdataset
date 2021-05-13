def inN():
    return int(input())
def inL():
    return list(map(int,input().split()))
def inNL(n):
    return [list(map(int,input().split())) for i in range(n)]

a,b,c,k = inL()
cnt = 0
if k >= a:
    cnt += a
    k -= a
else:
    cnt += k
    print(cnt)
    exit()

k -= b

if k>0:
    cnt -= k

print(cnt)