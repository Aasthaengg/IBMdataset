N = int(input())

an = list(map(int,input().split()))

boolian = True

for i in range(N):
    if an[i] % 2 == 0:
        if an[i] % 3 ==0 or an[i] % 5 ==0:
            boolian = True
        else:
            boolian = False
            break
if boolian == False:
    print('DENIED')
    
if boolian == True:
    print('APPROVED')