n = int(input())
a = list(map(int,input().split()))
m = sum(a)/ n
index = 0
for i in range(1,n):
  if abs(m-a[index])>abs(m-a[i]):
    index = i
print(index)