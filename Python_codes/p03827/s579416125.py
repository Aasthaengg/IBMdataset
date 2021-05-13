N = int(input())
S = input()
x = 0
ans = 0
for i in range(N):
    if S[i] == 'I':
        x += 1
        if x > ans:
            ans = x
    else:
        x -= 1
print(ans)
