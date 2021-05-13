def main():
    W = ['Sunny', 'Cloudy', 'Rainy']
    S = input()
    i = (W.index(S) + 1) % 3
    print(W[i])


if __name__ == '__main__':
    main()
