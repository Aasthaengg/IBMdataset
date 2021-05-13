N = int(input())

def  DigitsSum(n):
    s = 0
    while True:
        if n // 10 != 0:
            s += n % 10
            n = n // 10
        else:
            s += n
            break
    return s

S = 0

for i in range(1,int(N/2)+1):
    A = i
    B = N - i
    if S == 0 :
        S = DigitsSum(A)+DigitsSum(B)
    else:
        if S > DigitsSum(A)+DigitsSum(B):
            S = DigitsSum(A)+DigitsSum(B)
        else:
            continue

print(S)
