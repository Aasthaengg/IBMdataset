n=int(input())
a = [input() for _ in range(n)]
a.sort()
dict = {}
count = 0
for i in range(n):
  k = a[i]
  if (k in dict):
    count-=dict[k]
    dict[k]=1-dict[k]
    count+=dict[k]
  else:
    dict[k]=1
    count+=1
print(count)