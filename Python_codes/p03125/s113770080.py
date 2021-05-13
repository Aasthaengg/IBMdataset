a, b = map(int, input().split())
if a == b:
    print(a + b)
elif b % a == 0:
    print(a + b) 
else:
    print(b-a)