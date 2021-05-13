a , b = map(int,input().split())
cou = 0
for i in range(1,13):
    if a > i:
        cou += 1
    elif a == i and b >= i:
        cou += 1
    else:
        break
print(cou)