def main():
    n = int(input())
    A = list(map(int, input().split()))
    count = 0
    plus = '-1'
    A = [A[i + 1] - A[i] for i in range(n - 1)]
    for a in A:
        if plus == '-1':
            if a > 0:
                plus = True
            elif a < 0:
                plus = False
            else:
                pass
        elif plus:
            if a < 0:
                plus = '-1'
                count += 1
            else:
                pass
        else:
            if a > 0:
                plus = '-1'
                count += 1
            else:
                pass
    print(count + 1)

if __name__ == '__main__':
    main()
