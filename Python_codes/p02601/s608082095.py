A,B,C=map(int,input().split())
K=int(input())
abc=[A,B,C]
#赤＜緑＜青
for _ in range(K):
    if abc[0]>=abc[1]:
        abc[1]=abc[1]*2
    elif abc[1]>=abc[2]:
        abc[2]=abc[2]*2
    else:
        print("Yes")
        exit()

if abc[0]<abc[1] and abc[1]<abc[2]:
    print("Yes")
else:
    print("No")
