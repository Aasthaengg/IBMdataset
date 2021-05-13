def main():
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        ta, tb = [int(i) for i in input().split()]
        a.append(ta)
        b.append(tb)
    a = sorted(a)
    b = sorted(b)

    if n % 2:
        mid_idx = (n + 1)//2 -1
        print(b[mid_idx] -a[mid_idx] + 1)
    else:
        mid_idx = [n//2 - 1, n//2]
        mid_a = (a[mid_idx[1]] + a[mid_idx[0]])
        mid_b = (b[mid_idx[1]] + b[mid_idx[0]])
        print(mid_b - mid_a + 1)

if __name__ == '__main__':
    main()

