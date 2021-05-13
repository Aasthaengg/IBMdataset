
def main():
    a, b, k = map(int, input().split())
    r = set()
    for i1 in range(a, min(a + k, b)):
        r.add(i1)
    for i2 in range(max(a, b - k + 1), b + 1):
        r.add(i2)
    r = list(r)
    r.sort()
    for j in r:
        print(j)

if __name__ == '__main__':
    main()
