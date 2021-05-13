n=int(input())
lists=list(map(int,input().split()))
ans =0
SUMS=0
index=0
for l in range(n):
    while index < l or index< n and SUMS ^ lists[index] == SUMS + lists[index]:
        SUMS ^= lists[index]
        index+= 1
    ans += index-l
    SUMS ^= lists[l]
print(ans)