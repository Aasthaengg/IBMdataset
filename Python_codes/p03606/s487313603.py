
if __name__ == '__main__':
    a = int(input())
    count = 0

    for i in range(a):
        b, c = map(int, input().split())
        count += c-b+1

    print(count)