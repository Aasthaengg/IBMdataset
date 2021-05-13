n = int(input())
lasta = 0
firstb = 0
btoa = 0
cnt = 0
for _ in range(n):
    S = input()
    cnt += S.count('AB')
    if S[0] == 'B' and S[-1] != 'A':
        firstb += 1
    elif S[-1] == 'A' and S[0] != 'B':
        lasta += 1
    elif S[0] == 'B' and S[-1] == 'A':
        btoa += 1
if btoa == 0:
    print(cnt + min(lasta, firstb))
else:
    print(cnt + btoa + (min(firstb, lasta) if firstb + lasta > 0 else -1))
