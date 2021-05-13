def main():
    n = int(input())
    k = int(input())
    x = list(map(int, input().split()))

    dist = [min(abs(i-0), abs(i-k)) for i in x]
    print(sum(dist)*2)

main()