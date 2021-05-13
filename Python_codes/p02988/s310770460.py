n = int(input())
L = list(map(int, input().split()))


count = 0
for i in range(1,n-1):
    if min(L[i-1],L[i+1]) < L[i] < max(L[i-1], L[i+1]):
        count += 1
            
print(count)