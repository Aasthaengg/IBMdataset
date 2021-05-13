n = int(input())
s = str(input())
t = str(input())
if s == t:
    print(n)
else:
    for i in range(n):
        l = s[:i + 1] + t
        if l[:n] == s:
            print(len(l))
            break