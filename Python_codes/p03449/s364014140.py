n = int(input())
A1 = list(map(int,input().split()))
A2 = list(map(int,input().split()))

ans = 0
for i in range(n):
    x = sum(A1[0:i+1]+A2[i::])
    if ans < x:
        ans = x

print (ans)
