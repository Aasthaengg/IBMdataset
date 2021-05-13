a,b,c = map(int, input().split())
s = [a,b,c]
newlist = sorted(s)

if newlist[0]+newlist[1] == newlist[2]:
    print("Yes")

else:
    print("No")