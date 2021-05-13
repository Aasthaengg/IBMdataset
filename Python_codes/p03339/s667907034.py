N = int(input())
S = list(input())
e = S.count('E')
left = 0
right = e - (1 if S[0] == 'E' else 0)
ans = left + right

for i in range(N-1):
    if S[i+1] == 'E':
        right -= 1
    if S[i] == 'W':
        left += 1
    ans = min(ans, left+right)
            
print(ans)