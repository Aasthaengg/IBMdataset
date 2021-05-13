N=int(input())
a=list(map(int,input().split()))
dict={}
count=0
for i in a:
  if i not in dict:
    dict[i] = 1
    continue
  dict[i] += 1
for i,j in dict.items():
  if i > j:
    count += j
  elif i < j:
    count += j-i
print(count)