n,p = map(int,input().split())

ans = 0
s = input()
if p == 2 or p == 5:
    for i in range(len(s)):
        n = int(s[i])
        if n%p == 0:
            ans += i+1
    print(ans)
    exit()

r = [0]*p
r[0] = 1
t = 1
z = 0
for i in reversed(s):
    z = int(i) * t + z
    t *= 10
    t %= p
    z %= p
    r[z] += 1

ans = sum(i*(i-1)//2 for i in r)
print(ans)
