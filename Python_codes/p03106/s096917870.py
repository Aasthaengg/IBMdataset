a,b,k=map(int,input().split())
ii=1
ans=[]
while max(a,b)>=ii:
    if a%ii==0 and b%ii==0:
        ans.append(ii)
    ii+=1
print(ans[-k])