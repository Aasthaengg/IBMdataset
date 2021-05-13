N,K =list(map(int,input().split()))
H =sorted(list(map(int,input().split())))
print(sum(H[:-1*K]) if K > 0 else sum(H))
