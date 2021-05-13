from collections import Counter
def main():
    n = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    l1, l2 = 0, 0
    for k, v in c.items():
        if k > l1:
            if v >= 4:
                l1, l2 = k, k
            elif 2 <= v <= 3:
                l1, l2 = k, l1
            else:
                pass
        elif l2 < k <= l1 and v >= 2:
            l2 = k
    print(l1 * l2) 

if __name__ == '__main__':
    main()
