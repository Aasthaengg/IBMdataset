s = input()
ans = 0
Acnt = 0
cnt = 0
for c in s:
    if cnt <= 1 and c == "A":
        Acnt += 1
        cnt = 1
    elif c == "A":
        Acnt = 1
        cnt = 1
    elif cnt == 1 and c == "B":
        cnt = 2
    elif cnt == 2 and c == "C":
        ans += Acnt
        cnt = 1
    else:
        Acnt = 0
        cnt = 0
print(ans)