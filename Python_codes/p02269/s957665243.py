n = int(input())
d = {}
for i in range(n):
    c, s = input().split()
    if c == "insert":
        d[s] = 0
    else:
        if s in d:
            print("yes")
        else:
            print("no")
        
