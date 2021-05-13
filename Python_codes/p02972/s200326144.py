n = int(input())
a = [0]+list(map(int,input().split()))
b = [0]*(n+1)
for i in range(n,0,-1):
    b_sum = sum([b[i*j] for j in range(1,n//i+1)])
    b_sum %= 2
    if a[i] == 1 and b_sum == 0:
        b[i] = 1
    if a[i] == 0 and b_sum == 1:
        b[i] = 1
print(sum(b))
for i in range(1,n+1):
    if b[i]==1:
        print(i)