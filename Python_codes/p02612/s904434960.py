N = int(input())
num = N// 1000
mode = N % 1000
if mode == 0:
    print(0)
else:
    print((num + 1) * 1000 - N)