n = int(input())

l = set()

for _ in range(n):
    command, s = input().split()
    if command == "insert":
        l.add(s)
    else:
        if s in l:
            print("yes")
        else:
            print("no")
