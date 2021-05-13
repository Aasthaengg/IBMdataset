from collections import Counter
n=int(input())
a=[int(input()) for _ in range(n)]
a_count=Counter(a)
count=0
for i in a_count:
    if a_count[i]%2==1:
        count+=1
print(count)