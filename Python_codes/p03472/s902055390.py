import math
def main():
    n, h = list(map(int, input().split()))
    A, B = [], []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    a_max = max(A)
    B = list(filter(lambda x: x > a_max, B))
    B.sort(reverse = True)
    ans = 0
    for b in B:
        h -= b
        ans += 1
        if h <= 0:
            break
    else:
        ans += math.ceil(h / a_max)
    print(ans)

if __name__ == '__main__':
    main()
