n = int(input())
d,x = map(int, input().split())
ab = [int(input()) for _ in range(n)] #数字1*複数列入力

res = x
for i in range(n):
    c = ab[i]
    res += (d-1)//c +1

print(res)