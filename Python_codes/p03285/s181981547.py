N = int(input())
Flag = False
for Cake in range(0,26):
    for Doughnut in range(0,16):
        if 4*Cake+7*Doughnut==N:
            Flag = True
            break
    if Flag:
        break
if Flag:
    print('Yes')
else:
    print('No')