k,s = map(int,input().split())
f = 0
for i in range(k+1):
    for j in range(k+1):
        l = s-i-j
        if 0 <= l <=k:
            f+=1
print(f)