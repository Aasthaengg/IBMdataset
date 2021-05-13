a,b=map(int,input().split())
if (a>8 or b>8) and abs(a-b)>1:
    print(":(")
else:
    print("Yay!")