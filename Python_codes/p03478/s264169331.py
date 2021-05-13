n,a,b = map(int, input().split())
m = 0
for i in range(1,n+1):
    num = 0
    for h in str(i):
        num += int(h)
    if a <= num <= b:
        m += int(i)
print(m)