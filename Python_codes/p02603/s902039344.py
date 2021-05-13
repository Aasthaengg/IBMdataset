N = int(input())
a = list(map(int,input().split()))
num = 1000
flag = True
flag2 = True
for i in range(1,N):
  if a[i-1]<a[i] and flag == True:
    mi = a[i-1]
    ma = a[i]
    flag = False
  elif a[i-1]<a[i] and flag == False:
    ma = a[i]
  elif a[i-1]>a[i] and flag == False:
    num = (num//mi)*ma+(num%mi)
    flag = True
  if i == N-1 and flag == False:
    num = (num//mi)*ma+(num%mi)
print(num)