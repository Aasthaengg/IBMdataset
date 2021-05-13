nf = int(input())
hf = list(map(int, input().split()))

h = [hf[0]]
for i in range(1, nf):
    if hf[i] == hf[i - 1]:
        continue
    else:
        h.append(hf[i])
n = len(h)

if n == 1:
    print('Yes')
elif n == 2:
    if h[1] - h[0] >= -1:
        print('Yes')
    else:
        print('No')
else:
    if h[1] - h[0] < -1:
        print('No')
    else:
        for i in range(1, n - 1):
            if h[i] <= h[i + 1]:
                continue
            elif h[i + 1] - h[i] == -1:
                if h[i] - h[i - 1] >= 1:
                    h[i] -= 1
                    continue
                else:
                    print('No')
                    break
            else:
                print('No')
                break
        else:
            print('Yes')