n = int(input())
s = input()
t = input()
if s == t:
    print(len(s))
    exit()
for i in range(1, n):
    if s[i:] == t[:-i]:
        print(len(s) + i)
        break
else:
    print(len(s) * 2)