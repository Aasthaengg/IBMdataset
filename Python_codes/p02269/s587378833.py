n = int(input())
dic = {}

for _ in range(n):
    q, X = input().split()
    if q == "insert":
        dic[X] = 1
    else:
        if X in dic.keys():
            print("yes")
        else:
            print("no")