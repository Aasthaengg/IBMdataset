n = int(input())
A  = list(map(int, input().split()))
if sum(A)==0:
    print('Yes')
    exit()
if n%3==0:
    a=A[0]
    for i in range(1,n):
        a = a^A[i]
    if a==0:
        print('Yes')
        exit()
print('No')