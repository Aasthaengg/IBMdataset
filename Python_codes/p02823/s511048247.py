n,a,b = map(int,input().split())

margin = abs(a-b)

if (a % 2 == 0 and b % 2 == 0) or (a % 2 == 1 and b % 2 == 1):
    print(margin//2)
else:
    t = min(a-1, n-b) + 1 +(b-a-1)//2
    print(t)