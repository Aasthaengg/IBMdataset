def main():
    n = input()
    for _ in range(0,n):
        arr = map(int,raw_input().split())
        arr.sort()
        if arr[2] * arr[2] == arr[0] * arr[0] + arr[1] * arr[1]:
            print "YES"
        else:
            print "NO"

if __name__ == '__main__':
    main()