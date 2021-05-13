N,A,B=[int(x) for x in input().rstrip().split()]
l=[int(x) for x in input().rstrip().split()]
ans=0

for i in range(N-1):
    if((abs(l[i]-l[i+1]))*A)<=B:
        ans+=(abs(l[i]-l[i+1]))*A
    
    else:
        ans+=B
print(ans)
