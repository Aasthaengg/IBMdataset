n = int(input())
a = map(int, input().split())

odd = 0
for i in a:
	if i % 2 == 1: odd += 1
print('YES' if odd % 2 == 0 else 'NO')