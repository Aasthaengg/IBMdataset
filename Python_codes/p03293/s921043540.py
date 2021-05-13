S=input()
T=input()

ans = "No"
for i in range(len(S)):
	if S[i:] + S[0:i] == T:
		ans = "Yes"

print(ans)
