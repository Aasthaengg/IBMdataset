# A - Limited Insertion

N,b = int(input()),list(map(int,input().split()))
a = list([])
judge = 1

for i in range(N):
    j = N-i
    while j>0 and b[j-1]!=j:
        j -= 1
    if j==0:
        judge = 0
        break
    else:
        b.pop(j-1)
        a.append(j)

if judge==0:
    print(-1)
else:
    for i in range(N):
        print(a[N-1-i])