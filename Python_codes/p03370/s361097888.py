n,x = map(int, input().split())

ab = [int(input()) for _ in range(n)] #数字1*複数列入力

sab = sum(ab)
mab = min(ab)

print((x-sab)//mab+n)