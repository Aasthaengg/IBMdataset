s = input()
n = int(input())
for i in range(n):
    t = input().split()
    cmd, a, b = t[0], int(t[1]), int(t[2])
    if cmd == "print":
        print(s[a:b+1])
    elif cmd == "reverse":
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    else:
        s = s[:a] + t[3] + s[b+1:]
