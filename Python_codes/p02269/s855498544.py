mp = {}
for _ in range(int(input())):
    op, x = input().split()
    if op == "insert":
        mp[x] = True
    else:
        print(['no', 'yes'][x in mp])
