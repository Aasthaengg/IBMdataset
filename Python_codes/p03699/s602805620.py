N = int(input())
s = []
for i in range(N):
    s.append(int(input()))

s.sort()
x = sum(s)

if str(x)[-1] != '0':
    print(x)
    exit()

ans = x
for i in range(N):
    ans = max(x-s[i], ans-s[i])
    if str(ans)[-1] != '0':
        print(ans)
        exit()
print(0)
