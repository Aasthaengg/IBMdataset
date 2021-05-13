S, w = input(), int(input())
ans = ""
for i in range(len(S)):
	if i % w == 0:
		ans += S[i]
print(ans)
