X, Y = map(int, input().split())
ans='No'
if Y % 2 == 0 and 0 <= (4 * X - Y) / 2 <= X:
    ans='Yes'
print(ans)