n = int(input())
a = list(map(int, input().split()))

aa = [[a[i], i] for i in range(n)]
aa.sort()

print(' '.join(str(aa[i][1] + 1) for i in range(n)))