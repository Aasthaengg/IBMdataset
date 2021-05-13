N = int(input())
s = input()
t = input()
ans = N
if s == t:
    print(ans)
    exit()
if N == 1:
    print(ans*2)
    exit()
ans += 1
for i in range(1, N):
    if s[i:] == t[:-1*i]:
        print(ans)
        exit()
    ans += 1
print(ans)