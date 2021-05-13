if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    diff = a[1]-a[0]
    count =0
    for i in range(diff):
        count+=i

    print(count-a[0])