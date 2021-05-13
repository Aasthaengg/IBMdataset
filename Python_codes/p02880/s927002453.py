def main():
    N = int(input())
    l = [2, 3, 4, 5, 6, 7, 8, 9]
    if N == 1:
        print('Yes')
        return
    for i in range(8):
        c = N // l[i]
        r = N % l[i]
        if c > 0 and c < 10 and r == 0:
            print('Yes')
            return
    print('No')
main()