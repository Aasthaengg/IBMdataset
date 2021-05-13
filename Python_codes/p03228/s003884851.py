A,B,K = map(int, input().split())

giveA = int(A/2)
giveB = int(B/2)
for i in range(K):
    if i%2 == 0:
        giveA = int(A/2)
        A = giveA
        B += giveA
    else:
        giveB = int(B/2)
        B = giveB
        A += giveB

print(A,B)