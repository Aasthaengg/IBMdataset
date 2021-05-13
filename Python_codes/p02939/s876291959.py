S = input()
mae = 1
ato = 1
ls = len(S)

temp = S[0]
ans = 1
while True:
    ato += 1
    if ato > ls:
        break
    if temp != S[mae:ato]:
        ans += 1
        temp = S[mae:ato]
        mae = ato
print(ans)