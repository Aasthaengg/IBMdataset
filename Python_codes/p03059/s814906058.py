a,b,t = map(int,input().split())
x = 0
for i in range(100):
    if a * i <= t: x = i
print(x * b)