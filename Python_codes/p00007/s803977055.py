# AOJ 0007 Debt Hell
# Python3 2018.6.7 bal4u

a = 100000;
n = int(input())
while n > 0:
	n -= 1
	a = a + (a * 5) // 100
	a = ((a - 1) // 1000 + 1) * 1000   # 1000未満の切り上げ
print(a)
