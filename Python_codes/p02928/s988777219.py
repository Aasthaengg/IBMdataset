n, k = map(int, input().split())
lis = list(map(int, input().split()))
c1, c2 = 0, 0
for i in range(n):
        for j in range(n):
                if lis[i] > lis[j]:
                        c2 += 1
                        if j > i:
                                c1 += 1
ans = c1*k + c2*k*(k-1)//2
print(ans % 1000000007)