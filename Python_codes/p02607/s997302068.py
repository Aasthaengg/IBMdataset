def main():
    N = int(input())
    a = list(map(int,input().split(' ')))
    total = 0
    for i in range(N):
        if i % 2 == 0 and a[i] % 2 == 1:
            total += 1
    print(total)
main()