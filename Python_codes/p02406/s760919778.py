def hitoketame3(num):
    if num % 10 == 3:
        return True
    else:
        return False

n = int(input())
for i in range(1, n+1):
    x = i
    if x % 3 == 0:
        print(" {0}".format(i),end="")
        continue
    if hitoketame3(x) == True:
        print(" {0}".format(i),end="")
        continue
    while x != 0:
        x = x // 10
        if hitoketame3(x) == True:
            print(" {0}".format(i),end="")
            break
print("")