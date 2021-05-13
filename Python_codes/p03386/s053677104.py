s = input().split()
a = int(s[0])
b = int(s[1])
k = int(s[2])




for i in range(a, min(b, a + k - 1) + 1):
    print(i)
for i in range(max(b - k + 1, a + k), b + 1):
    print(i)
