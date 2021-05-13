N,M = map(int,input().split())
H = list(map(int, input().split()))
AB = [list(map(int,input().split()))for i in range(M)]
good = [True]*N
for i in range(M):
        a,b = AB[i]
        if H[a-1] > H[b-1]:
            good[b-1] = False
        elif H[a - 1] < H[b - 1]:
            good[a - 1] = False
        else:
            good[a - 1] = False
            good[b - 1] = False
#print(good)
print(good.count(True))