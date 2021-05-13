V = list(map(int, input().split()))
if V[0] == V[1]:
    print(V[2])
elif V[0] == V[2]:
    print(V[1])
else:
    print(V[0])
