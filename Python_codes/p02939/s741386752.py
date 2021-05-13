S = input()
N = len(S)
ans = 1
i = 1
prev_two = 0
while i < N:
    if prev_two:
        i += 1
        prev_two = 0
    elif S[i] == S[i-1]:
        i += 2
        prev_two = 1
    else:
        i += 1
    ans += 1
if i == N+1:
    ans -= 1
print(ans)