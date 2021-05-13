N = int(input())
res = 0
i =1
while i*i <= N:
    if N%i==0 and N//i-1>i:
        res += N//i - 1
    i += 1
print(res)