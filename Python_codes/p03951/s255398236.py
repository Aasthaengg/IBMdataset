n = int(input())
s = input()
t = input()
for i in range(n+1):
    k = s[:i] + t
    if k[:n] == s:
        print(n+i)
        break