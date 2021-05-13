n = int(input())
t,a = map(int,input().split())
h = [0] + list(map(int,input().split()))
kion = 99999
ans = 0
for i in range(1,n+1):
    tmp = t-h[i]*0.006
    #print(i,a,tmp,abs(a-tmp),kion,ans)
    if abs(a-tmp)<kion:
        kion = abs(a-tmp)
        ans = i
print(ans)
