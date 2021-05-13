n, k = map(int, input().split())
a_l = list(map(int, input().split()))
i = 0
while i < n:
    if i >= k:
        if a_l[i] > a_l[i-k]:
            print('Yes')
        else:
            print('No')
    i+=1