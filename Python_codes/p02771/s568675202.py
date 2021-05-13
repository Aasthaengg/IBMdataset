a,b,c = map(int,input().split())
if ((a == b and a != c) or (b == c and a != c)) or (c == a and b != a):
    print("Yes")
else:
    print("No")