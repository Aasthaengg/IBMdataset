P, Q, R = map(int, input().split())
if P >= Q and P >= R:
    print(Q + R)
elif Q >= P and Q >= R:
    print(P + R)
else:
    print(P + Q)