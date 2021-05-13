n = int(input())
l = list(map(int, input().split()))

ls = sorted(l)
k = (ls[n//2-1] + ls[n//2])/2

for i in range(n):
    if l[i] < k:
        print(ls[n//2])
    else:
        print(ls[n//2-1])