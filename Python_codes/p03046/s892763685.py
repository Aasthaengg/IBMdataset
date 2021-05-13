m,k=map(int,input().split())
if k>=2**m:
    print(-1)
    quit()
elif m==1:
    if k==0:
        print("0 0 1 1")
    else:
        print(-1)
    quit()
a=[i for i in range(0,k)]+[i for i in range(k+1,2**m)]
print(" ".join(map(str,a[::-1]+[k]+a+[k])))