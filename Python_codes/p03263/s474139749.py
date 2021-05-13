h,w=map(int,input().split())
hw=[[]]
ans=[]
for i in range(h):
    ht=[0]+list(map(int,input().split()))
    hw.append(ht)
for i in range(1,h+1):
    for j in range(1,w):
        if hw[i][j]%2==1:
            ans.append([i,j,i,j+1])
            hw[i][j+1]+=1

for k in range(1,h):
    
    if hw[k][-1]%2==1:
        ans.append([k,w,k+1,w])
        hw[k+1][-1]+=1
print(len(ans))
for i in ans:
    for j in range(len(i)):
        i[j]=str(i[j])
    print(" ".join(i))