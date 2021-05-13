def main():
    K, T = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    greatest = a[0]
    others = sum(a[1:])

    if greatest - others <= 1:
        print(0)
        return
    else:
        print(greatest-others-1)
        return

if __name__ == '__main__':
    main()
