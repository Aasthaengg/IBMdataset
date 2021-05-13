n = input()
for i in range(int(n)):
    a,b,c = list(map(int,input().split()))
    a,b,c = int(a),int(b),int(c)
    if a**2 + b**2 == c**2 or c**2 + a**2 == b**2 or b**2 + c**2 == a**2:
        print("YES")
    else:
        print("NO")
