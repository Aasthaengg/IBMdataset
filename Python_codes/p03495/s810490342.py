n,k=[int(i) for i in input().split()]

a_list=[int(i) for i in input().split()]
#print(a_list)

dic={}
for i in a_list:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

#print(dic)
#print(len(dic))


#書き換えなくてよい    
if len(dic)<=k:
    print(0)
else:
    ans=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    b_list=ans[k:]
    ans_sum=0
    for i in b_list:
        ans_sum+=i[1]
    print(ans_sum)
    
