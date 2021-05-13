import collections
N=int(input())
a=list(map(int,input().split()))
l=[]
if max(a)==0:
    print("Yes")
elif (N%3)==0:
    c=collections.Counter(a)
    values = list(c.values())  # aのCollectionのvalue値のリスト(n_1こ、n_2こ…)
    key = list(c.keys())  # 先のvalue値に相当する要素のリスト(要素1,要素2,…)
    for i in range(len(key)):
        l.append([key[i], values[i]])  # lは[要素i,n_i]の情報を詰めたmatrix
    l.sort(key=lambda x:x[1],reverse=True)
    #print(l)
    if (len(l)==3)and(l[0][1]==l[1][1]==l[2][1])and(l[0][0]^l[1][0]==l[2][0]):
        print("Yes")
    elif (len(l)==2)and(l[0][1]==2*l[1][1])and(l[1][0]==0):
        print("Yes")
    else:
        print("No")
else:
    print("No")