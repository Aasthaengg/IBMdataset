# N>=x>=0
# return max(floor(A*x/B)-A*floor(x/B))
# floor(t) は実数t以下の最大の整数
# x = Nの時が最大
# x/Bが一の直前になるようにとってみる
A, B, N = [int(i) for i in input().split()]
x = 0
if N >= B:
    x = B-1
else:
    x = N 
y = (A * x)// B - A * (x//B)
print(y)