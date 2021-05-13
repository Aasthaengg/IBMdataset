A = list(map(int, input().split()))
a = sorted(A)
k = str(a[-1])+str(a[1])
print(int(k)+a[0])
