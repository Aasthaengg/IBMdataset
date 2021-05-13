n = int(input())
a = list(map(int, input().split()))

def f(isPosi):
    total = 0
    cnt = 0
    for i in a:
        total += i
        if isPosi:
            if total >= 0:
                cnt += 1 + total
                total = -1
            isPosi = False
        else:
            if total <= 0:
                cnt += 1 - total
                total = 1
            isPosi = True
    return cnt

print(min(f(True), f(False)))