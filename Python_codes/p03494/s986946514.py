x = int(input())
y = [int(n) for n in input().split()]

ini = 0

def search(li):
    L = len(li)
    for i in range(L):
        if li[i]%2 != 0:
            return False
        else:
            li[i] = li[i]//2
    return True


while True:
    if search(y):
        ini += 1
    else:
        break

print(ini)

