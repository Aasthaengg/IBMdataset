n,k = map(int,input().split())
A = list(map(int,input().split()))

allvote=0
allvote=sum(A)
# print( allvote )

c=0
for a in A:
    if a>=allvote/(4*k) :
        c+=1

if c>=k :
    ans = "Yes"
else:
    ans = "No"
print(ans)