N = int(input())
# 2 <= N < 4500　くらいが保証されている

for h in range(3501):
    for w in range(3501):
        if 4*h*w-N*w-N*h <= 0:continue
        if N*h*w % (4*h*w-N*w-N*h) == 0:
            print(h,w,N*h*w // (4*h*w-N*w-N*h))
            exit()