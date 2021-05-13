n=int(input())
a=list(map(int,input().split()))

add=[]
sub=[]
for i in range(n):
    add.append(i+a[i])
    sub.append(i-a[i])

add_dic={}
sub_dic={}

for l in add:
    if l in add_dic:
        add_dic[l]+=1
    else:
        add_dic[l]=1

for l in sub:
    if l in sub_dic:
        sub_dic[l]+=1
    else:
        sub_dic[l]=1

ans=0

for i,k in add_dic.items():
    if i in sub_dic:
        ans+=k*sub_dic[i]

print(ans)