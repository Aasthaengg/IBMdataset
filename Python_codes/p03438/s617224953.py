def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    suma = sum(a)
    sumb = sum(b)
    k = sumb - suma

    s = [0] * N
    t = [0] * N
    for i in range(N):
        diff = a[i] - b[i]
        if diff < 0:
            if diff % 2 == 1:
                s[i] += (abs(diff)+1)//2
                t[i] += 1
            else:
                s[i] += abs(diff)//2
        else:
            t[i] += diff
    sums = sum(s)
    sumt = sum(t)
    remains = k - sums
    remaint = k - sumt
    if remains < 0 or remaint < 0:
        print('No')
        return
    if remains == 0 and remaint == 0:
        print('Yes')
        return
    if remains * 2 == remaint:
        print('Yes')
        return

if __name__ == "__main__":
    main()
