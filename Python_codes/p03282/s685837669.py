S = input()
K = int(input())
ans = 1
for i, s in enumerate(S):
    if i+1 == K:
        ans = s
        break
    if s == '1':
        continue
    else:
        ans = s
        break

print(ans)