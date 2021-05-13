n = int(input())
a = list(map(int, input().split()))
xor_all = 0
for i in range(n):
    xor_all = xor_all ^ a[i]
#print(xor_all)
for i in range(n):
    a[i] = a[i]^xor_all
print(*a)