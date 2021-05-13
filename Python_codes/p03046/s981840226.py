M, K = map(int,input().split())
if 2**M <= K or (M==1 and K==1):
    print(-1)
    exit()
elif K == 0:
    ls = [str(i//2) for i in range(2**(M+1))]
    print(" ".join(ls))
    exit()
ls = [str(i) for i in range(2**M)]
ls2 = [str(2**M-i-1) for i in range(2**M)]
ls.remove(str(K))
ls2.remove(str(K))
ls.append(str(K))
for elem in ls2:
    ls.append(elem)
ls.append(str(K))
print(" ".join(ls))
