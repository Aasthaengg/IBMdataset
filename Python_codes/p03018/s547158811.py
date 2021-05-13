s = input()
s = s.replace("BC", "D")
acnt = 0
mode = 1
ans = 0
"""
AD -> DA
AAD -> ADA -> DAA
ADAD -> DAAD -> DADA -> DDAA

Dを見る→前にあるAは何個？（その分だけ数える）
"""
for i in range(len(s)):
	if s[i] == "A":
		acnt += 1
	elif s[i] == "D":
		ans += acnt
	else:
		acnt = 0
print(ans)