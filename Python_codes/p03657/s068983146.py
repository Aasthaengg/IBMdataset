a, b = map(int, input().split())
ans = 'Impossible'
if (a+b) % 3 == 0:
    ans = 'Possible'
elif a % 3 == 0:
    ans = 'Possible'
elif b % 3 == 0:
    ans = 'Possible'
print(ans)