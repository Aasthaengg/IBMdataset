def mi():
    return map(int, input().split())

def main():
    A, B, K = mi()
    cnt = 0
    for i in range(min(A, B), 0, -1):
        if A%i == 0 and B%i == 0:
            cnt += 1
            if cnt == K:
                print(i)
                return

if __name__ == '__main__':
    main()