n = int(input())
internal_AB = 0
B_A = 0
B_ = 0
_A = 0
for i in range(n):
    s = input()
    for j in range(len(s)-1):
        if s[j] == 'A' and s[j+1] == 'B':
            internal_AB += 1
    if s[0] == 'B' and s[-1] == 'A':
        B_A += 1
    elif s[0] == 'B':
        B_ += 1
    elif s[-1] == 'A':
        _A += 1
if _A == 0 and B_ == 0:
    ans = max(0,B_A - 1)
elif _A == 0 or B_ == 0:
    ans = B_A
else:
    if B_A > 0:
        ans = B_A +1 + min(_A-1,B_-1)
    else:
        ans = min(B_,_A)
print(ans + internal_AB)



