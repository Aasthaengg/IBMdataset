s = input()
n = int(input())
for _ in range(n):
    t = [i for i in input().split()]
    if t[0] == "print":
        print(s[int(t[1]) : int(t[2]) + 1])
    elif t[0] == "reverse":
        s = s[:int(t[1])] + s[int(t[1]) : int(t[2]) + 1][::-1] + s[int(t[2]) + 1:]
    else:
        s = s[:int(t[1])] + t[3] + s[int(t[2]) + 1:]