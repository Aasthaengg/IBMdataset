import sys
n = int(input())
# 2, 4, 8, 16, 32, 64 | 128

# if n % 2 == 1:
#     print(0)
#     sys.exit()

if n == 1:
    print(1)


if 2 <= n and n < 4:
    print(2)
elif 4 <= n and n < 8:
    print(4)
elif 8 <= n and n < 16:
    print(8)
elif 16 <= n and n < 32:
    print(16)
elif 32 <= n and n < 64:
    print(32)
elif 64 <= n and n <= 100:
    print(64)
