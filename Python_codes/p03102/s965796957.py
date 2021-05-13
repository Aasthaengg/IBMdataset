n , m , c = map(int , input().split())
list_=[]
num=0
for a in range(n+1):
  list_.append(list(map(int , input().split())))
for b in range(1,n+1):
  sum_= c
  for d in range(m):
    sum_ = sum_ + (list_[0][d]*list_[b][d])
  if sum_ > 0:
    num = num + 1
print(num)