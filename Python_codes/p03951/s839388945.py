n = int(input())
s = input()
t = input()

a = 0
for i in range(n):
    if s[n - i - 1:] == t[:i + 1]:
        a = i + 1
print(n * 2 - a)
