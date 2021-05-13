#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

a, b = map(int, input().split())

if (b == 1):
    print(0)
    exit()
ans = 0
for i in range(1,1000000000):
    if (i == 1):
        b -= a
    else:
        b -= (a-1)
    ans += 1
    if (b <= 0):
        break
print(ans)


