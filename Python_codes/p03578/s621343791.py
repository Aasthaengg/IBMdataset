from collections import Counter

n=int(input())
d=Counter(list(map(int,input().split())))
m=int(input())
t=Counter(list(map(int,input().split())))
flag=0
for key in t.keys():
    if key in d.keys():
        if d[key] < t[key]:
            flag=1
            break
    else:
        flag=1
        break
if flag: print("NO")
else: print("YES")