n = list(map(int, input().split()))
k = int(input())
lst = sorted(n, reverse=True)
ans = lst[0]*2**k+sum(lst[1::])
print(ans)