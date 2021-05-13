from sys import stdin
readline = stdin.buffer.readline

def watering(h):
    ans = min(h)
    hh = list(map(lambda x: x - ans, h))
    if len(set(hh)) == 1:
        return ans
    fs = 0
    for i, n in enumerate(hh):
        if n == 0:
            if i != fs:
                hhh = hh[fs:i]
                ans += watering(hhh)
                fs = i + 1
            else:
                fs = i + 1
    else:
        hhh = hh[fs:]
        if len(hhh) > 0:
            ans += watering(hhh)
    return ans

def main():
    N = int(readline().rstrip())
    H = list(map(int, readline().rstrip().split()))
    print(watering(H))

if __name__ == "__main__":
    main()
