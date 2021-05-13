a,b,c = list(map(int,input().split()))
if abs(b-a) < abs(c-a):
    print("A")
else:
    print("B")