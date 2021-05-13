s = input()
s = s.replace("BC", "X")
#"AX" -> "XA"

cnt = 0
ans = []
for i in range(len(s)):
    if s[i] == "A": cnt += 1
    elif s[i] == "X": ans.append(cnt)
    else: cnt = 0
print(sum(ans))