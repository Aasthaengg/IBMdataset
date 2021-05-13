A,B = map(int,input().split())

a = (A+B)%3
b = A % 3
c = B % 3

m = min(a,b,c)

if m == 0:
    print("Possible")
else:
    print("Impossible")