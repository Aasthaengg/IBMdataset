N = int(input())
S = list(input())
A = [0]
ans = 0
for s in S:
    if s == 'I':
        ans += 1
    else:
        ans -= 1
    A.append(ans)
print(max(A))