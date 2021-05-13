a, b = map(int, input().split())
a, b = min(a,b), max(a,b)
if a==1 and b==1:
    print(1)
elif a == 1:
    print(b-2)
else:
    print(  (a-2) * (b-2))
