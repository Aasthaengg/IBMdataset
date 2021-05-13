a,b = map(int,input().split())
if (a + b)%2 ==0:
    print(round((a + b) / 2))
else:
    print(round((a + b + 1) / 2))