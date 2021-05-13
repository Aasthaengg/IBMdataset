if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    if a[0] < sum(a[1:]):
        print("Yes")
    else:
        print("No")