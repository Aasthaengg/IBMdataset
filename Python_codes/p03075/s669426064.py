def main():
    a = [int(input()) for _ in range(6)]
    k = a[5]

    for i in range(5):
        for j in range(i+1,5):
            if (a[j] - a[i]) <= k:
                continue
            else:
                return ':('

    return 'Yay!'

print(main())
