N = int(input())
S = input()

ans = S.count('E')
if S[0] == 'E':
    ans -= 1

arr =[]
arr.append(ans)

for i in range(1,N,1):
    if S[i-1] == 'W':
        ans += 1
    if S[i] == 'E':
        ans -= 1
    arr.append(ans)

print(min(arr))
