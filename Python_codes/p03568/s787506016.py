n = int(input())
a = list(map(int,input().split()))
t = 1
for e in a:
    if e%2 == 0:
        t *= 2
    else:
        t *= 1

print(3**n-t)
