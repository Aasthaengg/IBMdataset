A,B,C = map(int,input().split())

startR = A % B
i = 1
while True:
    R = A*i % B
    if R == C:
        print("YES")
        break
    if i != 1:
        if R == startR:
            print("NO")
            break
    i += 1