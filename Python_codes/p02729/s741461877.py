N,M = list(map(int,input().split()))

#偶数＋偶数
a = N * (N-1) / 2
#偶数＋奇数
#奇数＋奇数
b = M * (M-1) / 2

print(int(a+b))