h = int(input())
w = int(input())
n = int(input())

for i in range(1, min(h,w) + 1):
    if i * max(h,w) >= n:
        print(i)
        exit()