N = int(input())
ls = list(map(int,input().split()))
ls2 = []
for i in range(N):
    ls2.append([i,ls[i]])

ls3 = sorted(ls2, key=lambda x: x[1])
ls4 = []
for i in ls3:
    ls4.append(i[0]+1)

L=[str(a) for a in ls4]
L = ' '.join(L)
print(L)