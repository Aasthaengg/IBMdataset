n = int(input())
data = set()
for _ in range(n):
    command = input().split()
    if command[0] == "insert":
        data.add(command[1])
    elif command[0] == "find":
        if command[1] in data:
            print("yes")
        else:
            print("no")
