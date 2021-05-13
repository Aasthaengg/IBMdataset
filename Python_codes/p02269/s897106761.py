N = int(input())
dic = {}
for _ in range(N):
    command, string = input().split()
    if command == "insert":
        dic[string] = 1
    else:
        if string in dic:
            print("yes")
        else:
            print("no")
