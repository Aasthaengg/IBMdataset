from sys import stdin, stdout
input = stdin.readline
print = stdout.write

n, k = map(int, input().split())
arr = [int(i) for i in input().split()]

bit = [0] * 44
for i in arr:
    for j, b in enumerate(bin(i)[2:].zfill(44)):
        bit[j] += (ord(b) - ord('0'))

#print(bit)
res = 0
for i in range(44):
    val = 2 ** (43 - i)
    if (n - bit[i]) > bit[i] and k >= val:
        res += (n - bit[i]) * val
        k -= val
    else:
        res += bit[i] * val
print(str(res))
