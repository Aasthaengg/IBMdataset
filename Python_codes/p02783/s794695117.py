a,b=map(int, input().split())

if a%b == 0:
    print(a//b)
if a%b != 0:
    print(a//b+1)