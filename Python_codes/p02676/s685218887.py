def Ii():return int(input())
def Mi():return map(int,input().split())
def Li():return list(map(int,input().split()))
 
k = Ii()
a = input()
m = len(a)
if k >= m:
  print(a)
else:
  print(a[:k],end="")
  print('...')