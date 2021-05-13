k=int(input())

n=50
a=[n+k//n-1]*n

for i in range(k%n):
    a[i]+=n
    for j in range(n):
        if i==j:
            continue
        a[j]-=1


print(n)
print(' '.join([str(c) for c in a]))