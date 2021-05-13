a,b = 0,0
n = int(input())
for _ in range(n):
    s,t = input().split()
    if s==t:
        a,b = a+1,b+1
    elif s<t:
        b += 3
    else:
        a += 3
print(a,b)
