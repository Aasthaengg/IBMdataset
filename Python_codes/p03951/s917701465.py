n = int(input())
s = input()
t = input()

if s == t:
    print(n)
    exit()

for i in reversed(range(n)):
    tmp = s + t[i:]
    if tmp.startswith(s) and tmp.endswith(t):
        print(len(tmp))
        exit()