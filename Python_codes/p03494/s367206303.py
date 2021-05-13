N = int(input())
As = list(map(int, input().split()))

res = 0
while True:
	odd = list(filter(lambda x: x % 2 == 1, As))
	if odd:
		break
	else:
		As = list(map(lambda x: x // 2, As))
		res += 1
print(res)
