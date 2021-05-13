n,a,b = map(int,input().split())
awin = "Alice"
bwin = "Borys"
Draw = "Draw"
if (b-a)%2 == 0:
    print(awin)
else:
    print(bwin)