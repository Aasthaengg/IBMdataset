X, Y = map(int, input().split())

ans = 'No'

for crane in range(X + 1):
    turtle = X - crane

    if 2*crane + 4*turtle == Y:
        ans = 'Yes'

print(ans)