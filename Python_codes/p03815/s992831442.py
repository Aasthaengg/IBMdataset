x = int(input())

ans = 0 - -x//11

if ans*11 - 5 >= x:
    ans = ans*2 - 1
else:
    ans *= 2

print(ans)