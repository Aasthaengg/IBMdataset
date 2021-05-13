X,Y = (int(T) for T in input().split())
Count = 0
for T in range(61):
    if X*(2**T)<=Y:
        Count += 1
    else:
        print(Count)
        break