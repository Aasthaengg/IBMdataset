def main():
    N = int(input())  
    A = list(map(int, input().split()))
    gyaku = 0
    for a in A:
        gyaku += 1/a
    print(1/gyaku)


if __name__ == '__main__':
    main()