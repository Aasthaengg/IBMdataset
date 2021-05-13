

n = int(input())
d = set()
for _ in range(n):
    cmd, data = input().split()
    if cmd == 'insert':
        d.add(data)
    else:
        if data in d:
            print("yes")
        else:
            print("no")
