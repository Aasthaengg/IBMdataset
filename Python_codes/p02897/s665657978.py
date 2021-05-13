N=int(input())
a=0
for i in range(N+1):
    if i%2 != 0:
        a += 1
print(a/N)