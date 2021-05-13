n=int(input())
a=list(map(int,input().split()))
ans=[]
for i in a:
    ct=0
    big=10**5
    while i%2==0:
        i=i/2
        ct+=1
    big=min(ct,big)
    ans.append(big)
b=sorted(ans)
print(b[0])