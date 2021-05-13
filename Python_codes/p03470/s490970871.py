n=int(input())
d=[int(input()) for i in range(n)]
dict={}
for i in range(n):
  dict[d[i]]=True
print(len(dict))