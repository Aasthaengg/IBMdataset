Num = 0
for T in range(int(input())):
    L,R = (int(X) for X in input().split())
    Num += R-L+1
print(Num)