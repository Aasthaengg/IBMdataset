#sequence growing easy
N=int(input())
a=[int(input()) for _ in range(N)]
answer=0
now_value=10**9
for i in range(N-1,-1,-1):
    if a[i]>i:
        answer=-1
        break 
    if a[i]==now_value-1:
        now_value-=1
    else:
        answer+=a[i]
        now_value=a[i]
for i in range(N-1):
    if a[i+1]-a[i]>1:
         answer=-1
         break
print(answer)