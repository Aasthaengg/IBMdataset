n=int(input())
a=[]
b=[]
for i in range(n):
    ai,bi=map(int,input().split())
    a.append(ai)
    b.append(bi)
a.sort()
b.sort()
if n%2==0:
    i=int(n/2)
    ans_a=(a[i]+a[i-1])/2
    ans_b=(b[i]+b[i-1])/2
    ans=(ans_b-ans_a+1)*2-1
    print(int(ans))
else:
    i=int((n-1)/2)
    ans_a=a[i]
    ans_b=b[i]
    ans=ans_b-ans_a+1
    print(ans)