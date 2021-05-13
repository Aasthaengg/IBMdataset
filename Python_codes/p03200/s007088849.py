S = input()

b_count = 0
ans = 0

for pos in range(len(S)):
    if S[pos] == 'B':
        b_count += 1
    else:
        ans += b_count

print(ans)