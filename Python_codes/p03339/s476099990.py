N = int(input())
S = input()
left = [0]
right = [S.count('E')]
for i in range(N):
    if S[i] == 'W':
        left.append(left[i]+1)
        right.append(right[i])
    else:
        left.append(left[i])
        right.append(right[i]-1)
ans = 1000000
for i in range(N):
    ans = min(ans, left[i]+right[i+1])
print(ans)
