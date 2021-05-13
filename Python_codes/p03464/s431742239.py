#Ice link game
import math
k=int(input())
lists=list(map(int,input().split()))
lists=lists[::-1]
maxi=2
mini=2
flag=True
for i in range(k):
    #maxiとminiについて更新をしてゆく
    a=lists[i]
    upper_bound=math.floor(maxi/a)
    lower_bound=math.ceil(mini/a)
    new_maxi=(upper_bound+1)*a-1
    new_mini=lower_bound*a
    if new_maxi<new_mini:
        flag=False
        break
    else:
        maxi=new_maxi
        mini=new_mini
if flag:
    print(mini,maxi)
else:
    print(-1)