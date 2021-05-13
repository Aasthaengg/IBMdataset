n,k=map(int, input().split())
s=input()

s_list=[]
for i in s:
    if i=="L":s_list.append(0)
    else:s_list.append(1)
start_num=s_list[0]
i=0
while k>0:
    if i>=n:break
    if s_list[i]!=start_num:
        k-=1
        while i<n and s_list[i]!=start_num:
            s_list[i]=start_num
            i+=1
    i+=1
ans=0
for i in range(n):
    if i+1<n and s_list[i]==1 and s_list[i+1]==1:
        ans+=1
    if i-1>=0 and s_list[i]==0 and s_list[i-1]==0:
        ans+=1
print(ans)