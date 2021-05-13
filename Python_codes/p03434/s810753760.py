N = int(input())
a = list(map(int, input().split()))
 
# ソートしたとき、Aliceは偶数(0,2,...)番目を、Bobは偶数(1,3,...)番目を取る
a = sorted(a, reverse=True)
A = 0
B = 0
for i in range(N):
  if i % 2 == 0: A += a[i]
  else: B += a[i]

print(A-B)