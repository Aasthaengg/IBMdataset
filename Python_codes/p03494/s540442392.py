#B - Shift only
N = int(input())
A = list(map(int,input().split()))

def div_2():
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] //=  2
        else :
            return False
    return A

count = 0
while True:
    if div_2() != False:
        count += 1
    else:
        break
print(count)