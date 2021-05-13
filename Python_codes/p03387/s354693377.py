def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    A, B, C = mi()
    m = max(A, B, C)
    s = sum([A, B, C])
    cnt = 0
    while True:
        if s%3==0 and s>=3*m:
            break
        s += 2
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()