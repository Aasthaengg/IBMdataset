N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]


def calc(num, a):
    cnt = 0
    for i, h in enumerate(a):
        x = h - num * B
        x = (x - 1) // (A - B) + 1
        if x > 0:
            cnt += x
    if cnt <= num:
        return True
    else:
        return False


start = 0
end = 10 ** 10

while end - start > 1:
    mid = (start + end) // 2
    if calc(mid, H[:]):
        end = mid
    else:
        start = mid

print(end)
