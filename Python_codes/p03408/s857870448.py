n=int(input())
dic={}

for i in range(n):
    s=input()
    if s not in dic:
        dic[s]=1
    else:
        dic[s]+=1
#print(dic)

m=int(input())
for i in range(m):
    t=input()
    if t in dic:
        dic[t]-=1
    
ans_list=sorted(dic.items(),key=lambda x:x[1],reverse=True)
#print(ans_list)

if ans_list[0][1]<0:
    print(0)
else:
    print(ans_list[0][1])
