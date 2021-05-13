A,B = map(int, input().split())

PB =[A, B]

L_PB = max(PB)
S_PB = min(PB)

coin1 = L_PB

L_PB -= 1

if S_PB <= L_PB:
    coin2 = L_PB

else:
    coin2 = S_PB

print(coin1 + coin2)
