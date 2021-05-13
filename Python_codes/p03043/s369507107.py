a,b=map(int, input().split())
ans = 0
p = 0

for i in range(1,a+1):
    c = i
    while c < b:
        c = c*2
        ans += 1
    p += 1/2**ans
    ans = 0

print(p/a)