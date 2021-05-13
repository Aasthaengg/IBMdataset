n,a,b = map(int,input().split())
h =[0]*n
for i in range(n):
    h[i]=int(input())

def hantei(now):
    ab=a-b
    nokori = sum(kiriage( max(0,hh-now*b) ,ab)//ab  for hh in h)
    return nokori<=now
def kiriage(x,c):
    if x%c==0:
        return x
    else:
        return (x//c+1) *c

ma = 10**9 +1
mi = 1

while mi<ma:
    now=(mi+ma)//2
    which = hantei(now)
#     print(which,mi,now,ma)
    if which:
        ma=now
        ans=now
    else:
        mi=now+1
print(ans)