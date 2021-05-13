N,T = input().split()
T = int(T)
L = [int(x) for x in input().split()]
R = 0
for i in range(len(L) - 1):
    su = L[i+1] - L[i]
    R += min([su,T])
print(R+T)
