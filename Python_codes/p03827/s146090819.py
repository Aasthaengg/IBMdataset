N=int(input())
S=input()
x = 0
ans = x
for c in S:
    if c == 'I':
        x += 1
    elif c == 'D':
        x -= 1

    if x > ans:
        ans = x

print(ans)
