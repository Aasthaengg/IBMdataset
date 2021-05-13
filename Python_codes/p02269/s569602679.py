n = int(input())

dic = {}

for _ in range(n):
    command = input().split(" ")
    if command[0] == "insert":
        dic[command[1]] = 1
    else:
        if command[1] in dic:
            print("yes")
        else:
            print("no")