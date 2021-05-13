from collections import Counter

n=int(input())
lst=Counter(list(map(int,input().split())))
for i in range(1,n+1):
    if i in lst : print(lst[i])
    else : print(0)