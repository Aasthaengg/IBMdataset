from collections import defaultdict
dic=defaultdict(int)
n=int(input())
for _ in range(n): dic[input()]+=1
lis=sorted(dic.items(),key=lambda x:x[1],reverse=True)
M=lis[0][1]
ans=[]
for i in range(len(lis)):
    if lis[i][1]==M: ans.append(lis[i][0])
    else: break
ans.sort()
for i in ans: print(i)