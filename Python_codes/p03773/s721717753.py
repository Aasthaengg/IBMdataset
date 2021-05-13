a,b = map(int,input().split())

time = a + b
if time > 23:
    print(time - 24)
else:
    print(time)