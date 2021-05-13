x = int(input())
def sosuu(n):
    jud = 0
    for k in range(2,int(n**(0.5))):
        if n % k == 0:
            jud = 1
    if jud == 0:
        return True
    else:
        return False

for i in range(x,100004):
    if sosuu(i):
        print(i)
        break