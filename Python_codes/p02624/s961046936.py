# import time
N = int(input())
ssum = 0
# start = time.time()
for k in range(1, N + 1):
    X = int(N / k)
    ssum += k * X * (X + 1) / 2
print(int(ssum))
# elapsed_time = time.time() - start
# print("elapsed_time:{0}".format(elapsed_time) + "[sec]")