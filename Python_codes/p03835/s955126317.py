k,s=list(map(int, input().strip().split()))
f=0
for i in range(k+1):
    for j in range(k+1):
        if 0<=(s-i-j) and (s-i-j)<=k:
            f=f+1
print(f)