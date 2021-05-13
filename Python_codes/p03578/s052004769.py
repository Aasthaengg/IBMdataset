from collections import Counter
def main():
    n = int(input())
    D = list(map(int, input().split()))
    c1 = Counter(D)
    m = int(input())
    T = list(map(int, input().split()))
    c2 = Counter(T)
    for k, v in c2.items():
        if c1[k] < v:
            print('NO')
            exit()
    print('YES')

if __name__ == '__main__':
    main()
