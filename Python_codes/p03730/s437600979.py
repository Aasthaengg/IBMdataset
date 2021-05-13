A, B, C = list(map(int,input().split()))
r = ["NO" for i in range(B)]
for i in range(1,B+1):
    r[(A*i)%B] = "YES"
print(r[C])