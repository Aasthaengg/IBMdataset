

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    d, t, s = map(int, input().split())

    if (d / s) <= t:
        print('Yes')
    else:
        print('No')

