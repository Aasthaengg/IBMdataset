a,b,c,k = map(int, input().split())
over = 10**18
if abs(a-b)> over:
    print("unfair")
elif k %2 == 0:
    print(a-b)
else:
    print(b-a)
