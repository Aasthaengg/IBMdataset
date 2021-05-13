n = int(input())
s = set([])
for i in range(n):
    cmd, str1 = input().split()
    if cmd == "insert":
        s.add(str1)
    else:
        if str1 in s:
            print("yes")
        else:
            print("no")
