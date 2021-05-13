def main():
    N = int(input())
    d = list(map(int, input().split()))
    total = 0
    while len(d) > 1:
        c = d[0]
        for i in range(len(d) - 1):
            total = total + (c * d[1 + i])
        d.pop(0)
    print(total)
main()