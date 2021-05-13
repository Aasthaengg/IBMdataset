from math import gcd
n=int(input())
a=list(map(int,input().split()))
dic={}
for i,v in enumerate(a):
    dic[i+1]=v
#print(dic)
dic_sorted = list(sorted(dic.items(), key=lambda x:x[1]))
for i in range(n):
    if i!=n-1:
        print(dic_sorted[i][0],end=' ')
    else:
        print(dic_sorted[i][0])
