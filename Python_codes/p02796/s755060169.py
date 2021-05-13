import sys
readline = sys.stdin.buffer.readline
read = sys.stdin.buffer.read
 

N = int(readline())
XL = map(int, read().split())
 
LR = sorted(
    [(x - l, x + l) for x, l in zip(XL, XL)],
    key=lambda x: x[1])
LR = [(-3 * 10 ** 9, -3 * 10 ** 9)] + LR
 

i = 1
while True:
    if len(LR) <= i:
        break
 
    _, pr = LR[i - 1]
    cl, cr = LR[i]
 
    if pr <= cl:
        i += 1
    else:
        del LR[i]

print(len(LR) - 1)