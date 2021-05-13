X, Y = map(int, input().split())
ans = 'No'
if Y % 2 != 0:
    ans = 'No'
else:
    for i in range(X+1):
        a = X - i
        if a * 2 + i * 4 == Y:
            ans = 'Yes'
            break
print(ans)