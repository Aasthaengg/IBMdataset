dic = {}

n = int(input())

for i in range(n):
    op, key = input().split()
    h_key = hash(key) 
    if op == "insert":
        dic[h_key] = 1
    else:
        if h_key in dic:
            print("yes")
        else:
            print("no")