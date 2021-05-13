n = int(input())
s = input()
t = input()
for i in range(n):
    if s == t:
        print(len(s))
        exit()
    if s[i:] == t[:n-i]:
        print(len(s+t[-i:]))
        exit()
print(len(s+t))