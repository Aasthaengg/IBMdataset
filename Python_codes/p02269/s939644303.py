t = set()
m = int(input())
for i in range(m):
    cmd, key = input().split()
    if cmd == "insert":
        t.add(key)
    else:
        if key in t:
            print("yes")
        else:
            print("no")