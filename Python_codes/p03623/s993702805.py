x,a,b = map(int, input().split())
A = max(x,a) - min(x,a)
B = max(x,b) - min(x,b)
if A > B:
    print("B")
else:
    print("A")
