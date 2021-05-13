n = int(input())
a = input().split()
li = [int(i) for i in a]
s = min(li)
l = max(li)
p = sum(li)
print(s,l,p)
