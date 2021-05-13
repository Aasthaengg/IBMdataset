dic=dict()
n = int(input())
for i in range(n):
    a = input()
    t=a.split()
    if t[0] == "insert":
        dic[t[1]] = True
    else:
        if t[1] in dic:
            print("yes")
        else:
            print("no")