s = input()
q = int(input())
for _ in range(q):
    L = input().split()
    a, b = int(L[1]), int(L[2])
    if L[0] == 'print':
        print(s[a:b+1])
    elif L[0] == 'reverse':
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    elif L[0] == 'replace':
        s = s[:a] + L[3] + s[b+1:]