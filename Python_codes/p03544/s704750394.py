n=int(input())
lst=[2]
lst.append(1)
for i in range (2,n+1):
  lst.append(lst[-1]+lst[-2])
print(lst[n])
