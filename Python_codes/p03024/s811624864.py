
s = input()
i = 0
win = 0
lose = 0

for i in range(len(s)):
    if s[i] == "o":
        win  += 1
    else:
        lose += 1

if win + (15 - len(s)) >= 8:
    print("YES")
else:
    print("NO")
