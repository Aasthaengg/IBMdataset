n = int(input())
dictionary = set()

for _ in range(n):
    cmd, arg = input().split()
    if cmd == "insert":
        dictionary.add(arg)
    elif cmd == "find":
        if arg in dictionary:
            print("yes")
        else:
            print("no")