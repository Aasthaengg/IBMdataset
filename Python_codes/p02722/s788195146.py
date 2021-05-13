def divisors(x):
    div=[]
    for i in range(1,x+1):
        if i*i>x:
            break
        if x%i==0:
            div.append(i)
            if x%i!=i:
                div.append(x//i)
    return div

n=int(input())
ans=set([])
for k in divisors(n):
    if k==1:continue
    N=n
    while  N%k==0:
        N//=k
    N%=k
    if N==1:
        ans.add(k)

for j in divisors(n-1):
    if j==1:continue
    ans.add(j)
print(len(ans))