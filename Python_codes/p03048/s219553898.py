R,G,B,N = (int(x) for x in input().split())
maxr = N // R
maxg = N // G
count = 0
for i in range(maxr+1):
    for j in range(maxg+1):
        checker = N - (i*R + j*G)
        if checker // B >= 0:
            if checker % B == 0:
                count += 1
        elif checker == 0:
            count += 1
print(count)