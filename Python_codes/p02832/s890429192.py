def main():
    N = int(input())
    b = list(map(int, input().split()))
    i = 1

    for j in range(N):
        if b[j] == i:
            i += 1
    
    if i == 1:
        print(-1)
    else:
        print(N - i + 1)

if __name__ == '__main__':
    main()