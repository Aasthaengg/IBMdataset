n,k=list(map(int, input().split()))
h=list(map(int, input().split()))
h.sort()
out=0
for i in h:
    if i < k:
        out+=1
    else:    
        break
out=n-out
print(out)