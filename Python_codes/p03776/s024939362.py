import math
n,a,b=map(int,input().split())
v=list(map(int,input().split()))

# n,a,b=3,2,2
# v=[2,2,2]

v.sort(reverse=True)
am=0
for i in v[:a]:
    am+=i
maxv=am/a
B=v[a-1]
count=0
k=0
if v[0]==B:
    flag=0
else:
    flag=1

if flag==0:
    for i in range(n):
        if v[i]==B:
            k=i+1
            break
    k1=k
    while  k1<n+1 and v[k1-1]==B:
        count+=1
        k1+=1

    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    i=a-k+1 #Bを含める数
    ans=0
    while i<b-k+2 and i<count+1:
        ans+=combinations_count(count,i)
        i+=1


    print(maxv)
    print(ans)

else:
    for i in range(n):
        if v[i]==B:
            k=i+1
            break
    k1=k
    while  k1<n+1 and v[k1-1]==B:
        count+=1
        k1+=1

    def combinations_count(n, r):
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    i=a-k+1 #Bを含める数
    ans=combinations_count(count,i)
    print(maxv)
    print(ans)