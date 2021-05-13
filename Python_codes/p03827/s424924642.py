n = int(input())
s = input()
x = 0
answer = 0

for i in range(n):
	if s[i] == "I":
		x += 1
		if answer < x:
			answer = x
	elif s[i] == "D":
		x -= 1

print(answer)