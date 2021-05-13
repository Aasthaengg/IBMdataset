n = int(input())
k = int(input())
summ = 0
x = list(map(int, input().split()))
for i in x:
	summ += min(2*i, 2*(k-i))
print(summ)