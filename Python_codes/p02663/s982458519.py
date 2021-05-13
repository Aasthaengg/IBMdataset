m = list(map(int,input().split()))
l = m[0]*60
n = m[2]*60
s = l + m[1]
k = n + m[3]
a = k - s
print(a-m[4])