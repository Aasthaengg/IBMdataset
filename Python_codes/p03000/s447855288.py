
url = "https://atcoder.jp//contests/abc130/tasks/abc130_b"

def main():
    n,x = list(map(int, input().split()))
    lis = list(map(int, input().split()))
    lis.insert(0, 0)
    count = 0
    pos = 0
    for l in lis:
        pos += l
        count += 1
        if pos > x:
            print(count-1)
            exit()
    print(count)

if __name__ == '__main__':
    main()
