n = int(input())
a = list(map(int, input().split()))

# a[0]^a[1]^a[2] == 0
# a[1]^a[2]^a[3] == 0
# すなわち a[0] == a[3] と出来れば良い

# 1)すべて0
# 2) ある値が2n/3, 0がn/3
# 3) 3つの値がそれぞれn/3ずつ
b = list(set(a))
kind = len(b)
if kind == 1 and a[0] == 0:
    print('Yes')
    exit()
elif kind == 2 and a.count(0) == n//3 and n % 3 == 0:
    print('Yes')
    exit()
elif kind == 3:
    if a.count(b[0]) == a.count(b[1]) == a.count(b[2]) == n/3 and b[0] ^ b[1] ^ b[2] == 0:
        print('Yes')
        exit()
print('No')
