a,b,c = map(int,input().split())

oldCookies = []
oldCookies.append([a,b,c])

answer = 0

while(True):
	if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
		break 
	after_a = b / 2 + c / 2
	after_b = a / 2 + c / 2
	after_c = a / 2 + b / 2
	a = after_a
	b = after_b 
	c = after_c
	cookies = [a,b,c]
	answer += 1 
	
	for i in range(len(oldCookies)):
		if oldCookies[i] == cookies:
			answer = -1
			break

	if answer == -1:
		break

print(answer)