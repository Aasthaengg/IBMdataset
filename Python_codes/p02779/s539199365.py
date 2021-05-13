import collections
n = int(input())
a = list(map(int,input().split()))

li = collections.Counter(a)

li2 = [i for i in li.values()]

if max(li2)==1:
    print("YES")
else:
    print("NO")
    
