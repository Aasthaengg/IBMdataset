s = input()
q = int(input())

printlist = []

for _ in range(q):
    c = list(map(str, input().split()))
    start = int(c[1])
    end = int(c[2]) + 1

    if c[0] == "print":
        printlist.append(s[start:end])
    elif c[0] == "reverse":
        r = s[start:end]
        sr = r[::-1]
        s = s[:start] + sr + s[end:]
    elif c[0] == "replace":
        r = c[3]
        s = s[:start] + r + s[end:]

for p in printlist:
    print(p)
