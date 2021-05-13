N=int(input())

#bit探索
start=int((2*N+1)**0.5)

for i in range(3):
    i += start
    if i*(i+1) >= 2*N:
        ret = i
        delete=i*(i+1)/2 - N
        break

for k in range(1,ret+1):
    if k != delete:
        print(k)