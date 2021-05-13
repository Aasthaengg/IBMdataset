N = int(input())
A = 0
B = 0
AB = 0
ans = 0

for _ in range(N):
    S = list(input())

    for i in range(len(S)):
        try:
            if S[i] == 'A' and S[i+1] == 'B':
                ans += 1
        except:
            pass
    if S[0] == 'B':
        B += 1
        if S[-1] == 'A':
            A += 1
            AB += 1
    elif S[-1] == 'A':
        A += 1

if A == B and A == AB and AB != 0:
    print(A-1+ans)
else:
    print(min(A,B)+ans)