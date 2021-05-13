n=int(input())
low=[]
high=[]
for i in range(n):
    a,b=map(float,input().split())
    low.append(a)
    high.append(b)
low.sort()
high.sort()
if n%2==0:
    low_avg=(low[n//2-1]+low[n//2])/2
    high_avg=(high[n//2-1]+high[n//2])/2
    ans=(high_avg-low_avg)*2+1
else:
    ans=high[(n-1)//2]-low[(n-1)//2]+1
print(int(ans))