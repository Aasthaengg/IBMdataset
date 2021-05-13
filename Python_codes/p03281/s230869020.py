n = int(input())
t = 0
for i in range(1,n+1,2):
    num = 0
    for h in range(1,i+1):
        if i%h == 0:
            num += 1
    if num == 8:
        t += 1
print(t)