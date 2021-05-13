n,k = map(int,input().split())
a = list(map(int,input().split()))
b0 = [n]*41
b1 = [0]*41
ans = 0
temp = 0
for i in a:
    bit = bin(i)
    for j in range(len(bit)-2):
        t = (int(bit[-j-1]) == 1)
        b0[-j-1] -= t
        b1[-j-1] += t
# print(b1)
# print(b0)
for i in range(41):
    if temp + 2**(40-i) <= k and b0[i] > b1[i]:
        temp += 2**(40-i)
        ans += 2**(40-i) * b0[i]
    else:
        ans += 2**(40-i) * b1[i]

print(ans)