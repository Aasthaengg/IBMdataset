n = int(input())
A = list(map(int,input().split()))
index = 0
suml = 0
sumr = sum(A)
diff = sumr
ans = 0
for i in range(n):
    suml += A[i]
    sumr -= A[i]
    tmp  = abs(sumr -suml)
    if diff < tmp:
        ans = diff
        break
    diff = tmp
print(ans)
