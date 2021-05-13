if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    x = [int(i) for i in input().split()]
    y = [int(i) for i in input().split()]
    x.append(a[2])
    y.append(a[3])

    if min(y) > max(x):
        print("No War")
    else:
        print("War")