s=input()
K=int(input())
list=[]
for i in range(K):
  for j in range(len(s)-i):
    if s[j:j+i+1] not in list:
      list.append(s[j:j+i+1])
list.sort()
print(list[K-1])