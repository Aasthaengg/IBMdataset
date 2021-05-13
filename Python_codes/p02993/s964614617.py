# n, k = map(int, input().split())
# n = int(input())
# li = list(map(int, input().split()))
s = input()
flag = True
prev = ''
for i in s:
	if i == prev:
		flag = False
		break
	prev= i
print("Good" if flag else "Bad")