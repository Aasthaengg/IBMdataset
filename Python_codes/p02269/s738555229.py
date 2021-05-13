a = set()
n = int(input())
for i in range(n):
    s = input().split()
    if(s[0]=="insert"):
        a.add(s[1])
    else:
        if(s[1] in a):
            print("yes")
        else:
            print("no")