n = int(input())
l = list(map(int, input().split()))

i = 0
ans = 0
while i < n:
    j = i
    while j < n-1 and l[j] >= l[j+1]:
        j += 1
    k = i
    while k < n-1 and l[k] <= l[k+1]:
        k += 1
    i = max(j, k) + 1
    ans += 1
    #print(j, k)

print(ans)