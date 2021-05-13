N = input()
D = sorted(list(map(int,input().split())))
d1 = D[len(D)//2-1]
d2 = D[len(D)//2]

print(d2-d1)