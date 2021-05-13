a = int(input())

if a==1:
    print(1)
    exit()

res = 1
for i in range(2,32):
    for j in range(2,10):
        x = i**j
        if x > a:
            pass
        else:
            res = max(res,x)
print(res)