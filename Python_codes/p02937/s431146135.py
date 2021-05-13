# -*- coding: UTF-8 -*-
import math
import bisect
# f=open("test.txt")
# line=f.readline()
# lists=[]
# while line:
#     lists.append("".join(list(line)[:-1]))
#     line=f.readline()
# 
# f.close()
# 
# s=lists[0]
# t=lists[1]

s=input()
t=input()

alpha=list("abcdefghijklmnopqrstuvwxyz")

dic_s={alpha[i]:0 for i in range(26)}
dic_t={alpha[i]:0 for i in range(26)}

a={alpha[i]:[] for i in range(26)}
b={alpha[i]:[] for i in range(26)}


for i in range(len(s)):
  
    if dic_s[s[i]]==0:
        dic_s[s[i]]=+1
    a[s[i]].append(i+1)


for j in range(len(t)):
    
    if dic_t[t[j]]==0:
        dic_t[t[j]]=+1
    b[t[j]].append(j+1)
for i in range(26):
	a[alpha[i]].append(10**9)
flag=True

for i in range(26):
    if dic_t[alpha[i]]>0 and dic_s[alpha[i]]==0:
        flag=False

place=[0,0]

if flag:
    #文字を構成できる場合
    for i in range(len(t)):
        string=t[i]
        num=bisect.bisect_right(a[string],place[0])  
        if a[string][num]==10**9:
            place[1]+=1
            place[0]=a[string][0]
        else:
            place[0]=a[string][num]
  

    print(place[0]+place[1]*len(s))

else:
    #構成できない場合
    print(-1)
