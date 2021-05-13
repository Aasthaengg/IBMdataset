from collections import defaultdict
dic = defaultdict(int)
s = list(input())
for i in s:
    dic[i]+=1
b = True
for j in s:
    if dic[j]!=2:
        b=False
if b:
    print("Yes")
else:
    print("No")
