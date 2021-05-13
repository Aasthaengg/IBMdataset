a,b,c = map(int, input().split())
d = max(a,b,c)
x = d-a + d-b + d-c
if x % 2 == 0:
    print(x//2)
else:
    print((x+1)//2 + 1)