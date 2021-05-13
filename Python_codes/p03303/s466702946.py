S = list(input())
w = int(input())

ans_list = list()
ans = ' '

for i in range(0,int(len(S)),w):
	ans_list.append(S[i])

for x in ans_list:
	ans += x

print(ans)