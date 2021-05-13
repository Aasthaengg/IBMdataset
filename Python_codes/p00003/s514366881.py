n = int(input())
for _ in range(n):
    a,b,c = list(map(int,input().split()))
    if a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + c**2 == b**2 :
        print("YES")
    else :
        print("NO")
