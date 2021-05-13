N = int(input())
s = input()
t = input()

if s == t:
    print(N)
    exit(0)

for i in range(1, N):
    if s[i:] == t[:-i]:
        ans = s[:i] + s[i:] + t[-i:]
        print(len(ans))
        exit(0)

print(2 * N)
