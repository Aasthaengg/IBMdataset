n = int(input())
mydic = {}
for _ in range(n):
    s,t = input().split()
    if s == "insert":
        mydic[t] = 1
    else:
        if t in mydic.keys():
            print("yes")
        else:
            print("no")
