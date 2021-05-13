def main():
    n = int(input())
    a = list(map(int, input().split()))
    denom = 0
    for i in a:
        denom += (1 / i)
    print(1 / denom)
main()