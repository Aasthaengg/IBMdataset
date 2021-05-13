n = int(input())
l = list(map(int, input().split()))
l.sort()

# a, bをfixしてcを探索
# n*n*logn
# c_i < a+b をにぶたん
def binary_search(list, item):
    # listからitem未満の最大のindexを取得
    low = 0
    high = len(list) - 1
    if list[high] < item:
        return high+1
    if list[low] >= item:
        return low
    while True:
        mid = (low + high) //2
        guess = list[mid]
        if high - low <= 1:
            return high
        if guess >= item:
            high = mid
        else:
            low = mid

ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        a = l[i]
        b = l[j]
        c = binary_search(l, b+a)
        ans += c-(j+1)
print(ans)
