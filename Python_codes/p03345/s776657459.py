a, b, c, k = map(int, input().split())

if len(str(abs(a-b))) > 18:
    ans = 'Unfair'
else:
    ans = (a-b) * (-1)**(k%2)

print(ans)
