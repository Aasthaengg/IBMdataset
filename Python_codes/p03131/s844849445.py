

K,A,B=map(int, input().split())
#操作K回ビスケットを最大化
if A+2>=B:
    print(K+1)
    exit()

if 1+K-2<A:
    print(K+1)
    exit()

res=K-(A-1)
ans=A
if res%2==1:
    ans+=1
ans+=(res//2)*(B-A)

print(ans)