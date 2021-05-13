import collections
n=int(input())
c=collections.Counter(list(map(int,input().split()))).most_common()
a=0
for i in c:
 if i[0]>i[1]:a+=i[1]
 else:a+=i[1]-i[0]
print(a)