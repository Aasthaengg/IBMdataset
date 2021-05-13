import sys
N = int(input())
for h in range(1,3501):
    for w in range(1,3501):
        if 4*h*w - N*(w+h) > 0:
            if N*h*w / (4*h*w - N*(w+h)) % 1 == 0:
                print(h,w,int(N*h*w / (4*h*w - N*(w+h))))
                sys.exit()