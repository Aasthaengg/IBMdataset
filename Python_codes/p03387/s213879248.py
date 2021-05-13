a,b,c = map(int,input().split())
z = max(a,b,c)
x = z - a + z - b + z - c
if x % 2 != 0:
    x += 3
print(x // 2)