N = int(input())
a = list(map(int, input().split()))
#print(a)
b = [0]*(N)

for i in range(N, 0, -1):
    to = 0
    #print(i)

    for j in range(i-1, N ,i):
        to += b[j]

    if to%2 != a[i-1]:
        b[i-1] = 1
    #print(b)
if sum(b)==0:
    print(0)

else:
    print(sum(b))
    ans = str()
    for i in range(N):
        if b[i]:
            ans += str(i+1)+" "
    print(ans)