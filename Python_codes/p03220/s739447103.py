n = int(input())
T, A = list(map(int, input().split(" ")))
H = list(map(int, input().split(" ")))

def TEMP(H):
    return T - H*0.006

def AAA(H):
    return abs(A - H)

H = list(map(TEMP, H))

H = list(map(AAA, H))

print(H.index(min(H))+1)
