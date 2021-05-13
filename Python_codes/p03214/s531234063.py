N = int(input())
arr = list(map(int, input().split()))
ave = sum(arr) / N

ret = N
tmp = float("inf")
for i,flame in enumerate(arr):
    if abs(ave - flame) < tmp:
        tmp = abs(ave - flame)
        ret = i
print(ret)