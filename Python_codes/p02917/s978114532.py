
def main():
    n = int(input())
    b = list(map(int, input().split()))

    a = [0]*n

    for i,e in enumerate(b):
        if i == 0:
            a[0] = b[0]
        else:
            a[i] = min(b[i-1], b[i])

    a[-1] = b[-1]
            # if a[i] >= a[i+1] and e <= b[i-1]:
            #     a[i] = e
            # else:
            #     a[i+1] = e

    print(sum(a))

if __name__ == '__main__':
    main()