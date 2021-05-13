dic = {}
n = int(input())
for i in range(n):
    op, key = input().split()
    if op == "insert":
        dic[key] = 1
    else:
        if key in dic:
            print("yes")
        else:
            print("no")