import collections
n=int(input())
arr=[]
for i in range(n):
  a=int(input())
  arr.append(a)
c = collections.Counter(arr)
ans=0
for j in c.values():
    if j % 2 != 0:
        ans += 1
print(ans)