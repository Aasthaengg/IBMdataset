import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    drinks = list()
    ans = 0
    for _ in range(n):
        drinks.append(list(map(int, input().split())))
    drinks = sorted(drinks, key=lambda x: x[0])
    for drink in drinks:
        if drink[1] >= m:
            ans += drink[0] * m
            break
        else:
            ans += drink[0] * drink[1]
            m -= drink[1]
    print(ans)
            
if __name__ == '__main__':
    main()