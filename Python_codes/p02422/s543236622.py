s = input()

q = int(input())
query = []

for _ in range(q):
    query = input().split()
    if query[0] == 'replace':
        a, b = map(int, query[1:3])
        s = s[:a] + query[3] + s[b+1:]
    elif query[0] == 'reverse':
        a, b = map(int, query[1:3])
        r = s[b:a-1:-1] if a != 0 else s[b::-1]
        s = s[:a] + r + s[b+1:]
    elif query[0] == 'print':
        a, b = map(int, query[1:3])
        print(s[a:b+1])

