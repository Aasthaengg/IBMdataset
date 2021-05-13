N = int(input())
s = input()
t = input()

L = N - 1
for i in range(N):
    if (s[i:N + 1] == t[0:L + 1]):
        print(N * 2 - len(s[i:]))
        exit()
    L -= 1

print(N * 2)
