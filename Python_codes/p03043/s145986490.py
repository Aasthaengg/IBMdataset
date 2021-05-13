n,k = map(int,input().split())
win = 0
for i in range(1,n+1):
    a = 1
    while i*a < k:
        a *= 2
    win += 1/a
print(win/n)
