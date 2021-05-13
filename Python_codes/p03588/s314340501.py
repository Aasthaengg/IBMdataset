if __name__ == '__main__':
    a = int(input())
    max1 = 0
    max2 = 0
    for i in range(a):
        b, c = map(int, input().split())
        if max1<b:
            max1=b
            max2=c
    print(max1+max2)
