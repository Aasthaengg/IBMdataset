def binary_search(h, left, right, a,b):
    d = a-b
    while left + 1 < right:
        k = (left+right)//2
        cost = 0
        for i in h:
            tmp = i - k * b
            if tmp <= 0:
                continue
            cost += (tmp + d - 1) // d
        # print(left,right, k, cost)
        if cost > k:
            left = k
        else:
            right = k
    return right


n,a,b = map(int,input().split())
h = []
cnt = 0
for _ in range(n):
    i = int(input())
    h.append(i)
    cnt += (i+a-1)//a
print(binary_search(h, -1, cnt+1,a,b))
