
if __name__ == '__main__':
    b, c = map(int, input().split())

    min = 9999
    for i in range(b):
        a = [int(i) for i in input().split()]
        if  a[1]<= c and a[0] < min:
            min = a[0]

    if min == 9999:
        print("TLE")
    else:
        print(min)