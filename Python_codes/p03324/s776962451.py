def calc(x):
    ret = 0
    while x % 100 ==0:
        x /= 100
        ret += 1
    return ret

D, N = map(int, input().split())

cnt = 0
val = 0

while cnt < N:
    val += 1
    if calc(val) == D:
        cnt += 1

print(val)
