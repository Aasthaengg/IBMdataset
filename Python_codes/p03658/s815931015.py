
if __name__ == '__main__':
    b, c = map(int, input().split())
    a = [int(i) for i in input().split()]

    a.sort(reverse=True)
    count = 0
    for i in range(c):
        count+=a[i]
    print(count)