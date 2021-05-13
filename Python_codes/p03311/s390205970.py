N = int(input())
Alist = list(map(int, input().split()))
Alist = sorted([Alist[i] - i - 1 for i in range(N)])
if N%2 == 0:
    mid = (Alist[N//2-1]+Alist[N//2])//2
else:
    mid = Alist[N//2]
ans = sum([abs(a-mid) for a in Alist])
print(ans)