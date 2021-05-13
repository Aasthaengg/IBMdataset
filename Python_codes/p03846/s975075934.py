from collections import Counter
N=int(input())
A=list(map(int,input().split()))
l=[]
c=Counter(A)
flag=1
ans=1
values=list(c.values())	#aのCollectionのvalue値のリスト(n_1こ、n_2こ…)
key=list(c.keys())	#先のvalue値に相当する要素のリスト(要素1,要素2,…)
p=10**9+7
for i in range(len(key)):
    l.append([key[i],values[i]])#lは[要素i,n_i]の情報を詰めたmatrix
l.sort(key=lambda x:x[0])
for i in range(len(key)):
    if N%2==0:
        if (l[i][0]%2==1)and(0<l[i][0]<N)and(l[i][1]==2):
            ans=(ans*2)%p
        else:
            flag=0
            break
    else:
        if (l[i][0]==0)and(l[i][1]==1):
            ans=ans
        elif (l[i][0]%2==0)and(0<l[i][0]<N)and(l[i][1]==2):
            ans=(ans*2)%p
        else:
            flag=0
            break
if flag==1:
    print(ans%p)
else:
    print("0")