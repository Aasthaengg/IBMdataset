A=input()
ans=[]
count=0

for i in range(4):
    if A[i] not in ans:
        ans.append(A[i])
    else:
        count+=1

if count==2 and len(ans)==2:
    print("Yes")
else:
    print("No")
