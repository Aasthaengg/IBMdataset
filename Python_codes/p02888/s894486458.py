n = int(input())
l = list(map(int, input().split()))

s = 0

l.sort()

for i in range(n-2):
    j = n-2
    k = n-1
    while i < j:
        if l[k] >= l[i] + l[j] and j < k:
            #print(0, i, j, k)
            k -= 1
        else:
            #print(1, i, j, k)
            s += k - j
            j -= 1


print(s)
