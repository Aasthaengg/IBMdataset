words = list(input().split())


for i in range(len(words)-1):
	if words[i][-1] == words[i+1][0]:
		ans = 'YES'
	else:
		ans = 'NO'
		break
		
print(ans)

