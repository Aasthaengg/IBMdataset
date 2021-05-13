N = int(input())
A = int(input())

max_B = 10000//500

boolian = False

for b in range(max_B+1):
    if boolian == True:
        break
    for a in range(A+1):
        someone = 500*b + a 
        if someone == N:
            boolian = True
            break
        if someone != N:
            boolian = False
            continue
            
if boolian == True:
    print('Yes')
if boolian == False:
    print('No')