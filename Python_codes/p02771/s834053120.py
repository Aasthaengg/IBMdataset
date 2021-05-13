from collections import Counter
a=list(map(int,input().split()))
dic=Counter(a)
for i in dic.values():
    if i==2:
        print("Yes")
        exit()
print("No")
