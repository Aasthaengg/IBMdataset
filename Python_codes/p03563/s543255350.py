R = int(input())
G = int(input())

if R < G:
    print(R + 2*abs(G-R))
else:
    print(R - 2*abs(G-R))