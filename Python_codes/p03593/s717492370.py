import collections
H,W=map(int,input().split())
table=[list(input()) for _ in range(H)]
ch=[]
for i in range(H):
    for j in range(W):
        ch.append(table[i][j])
c=collections.Counter(ch)
values=list(c.values())	#aのCollectionのvalue値のリスト(n_1こ、n_2こ…)
key=list(c.keys())	#先のvalue値に相当する要素のリスト(要素1,要素2,…)
count4=0
count2=0
count1=0
for i in values:
    if i%4==0:
        count4=count4+1
    elif i%2==0:
        count2=count2+1
    else:
        count1=count1+1
if (H%2==0)and(W%2==0):
    if count2+count1==0:
        print("Yes")
    else:
        print("No")
elif (H%2==1)and(W%2==1):
    if (count2<=((H+W-2)//2))and(count1==1):
        print("Yes")
    else:
        print("No")
else:
    if H%2==0:
        nu=H//2
    else:
        nu=W//2
    if (count2<=nu)and(count1==0):
        print("Yes")
    else:
        print("No")

