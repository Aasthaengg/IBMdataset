import sys
input = sys.stdin.readline

n,k= map(int, input().split())
a= list(map(int, input().split()))

mod=10**9+7
# mod の逆元
def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

# 正,負 で分ける
b=[]
c=[]
for i in a:
    if i>=0:
        b.append(i)
    else:
        c.append(i)

b.sort(reverse=True)
c.sort()
ans=1
if k==n:
    for i in range(n):
        ans*=a[i]
        ans%=mod

elif k%2==1 and len(c)==n:
    c.sort(reverse=True)
    for i in range(k):
        ans*=c[i]
        ans%=mod

else:
    x=k
    # プラスの配列をどこまで進めたか
    v=0
    # マイナスの配列をどこまで進めたか？
    w=0
    if k%2==1:
        ans*=b.pop(0)
        k-=1

    for i in range(k):
        if x>=2:
            x-=2
            if v+2<=len(b) and w+2<=len(c):
                if b[v]*b[v+1]>c[w]*c[w+1]:
                    ans*=b[v]*b[v+1]
                    v+=2
                else:
                    ans*=c[w]*c[w+1]
                    w+=2


            elif v+2<=len(b):
                ans*=b[v]*b[v+1]
                v+=2

            else:
                ans*=c[w]*c[w+1]
                w+=2

            ans%=mod
            if x==0:
                break

print(ans)