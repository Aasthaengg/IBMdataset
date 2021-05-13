N = int(input())
s = input()
t = input()

if s == t:
    print(len(s))
    exit()

x = N-1
for i in range(1,N):
    if s[i:] == t[:-i]:
        break
    else:
        x -= 1

print(len(s) + len(t) - x)