N,K = map(int,input().split())
p=0
for i in range(1,N+1):
    jo = 0
    while True:
        if i*(2**jo) >= K:
            break
        jo += 1
    p += (1/N) * (1/2)**jo
print(p)
