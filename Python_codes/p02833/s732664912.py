import sys
n = int(input())
ans = 0
i = 1
if n%2 == 1:
    print(ans)
    sys.exit()

while True:
    d = 5**i
    if d > n//2:
        break
    else:
        ans += ((n//2) - (n//2)%d)//d
        i += 1
print(ans)