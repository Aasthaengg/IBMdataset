n,x = map(int, input().split())
m = [int(input()) for i in range(n)]
num = n
x -= sum(m)
num += x//min(m)
print(num)