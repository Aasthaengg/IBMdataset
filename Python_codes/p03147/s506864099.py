def main():
    n = int(input())
    # n, m = map(int, input().split())
    h = list(map(int, input().split()))
    # s = input()
    # h = [int(input()) for _ in range(n)]

    count = 0
    h.append(0)
    for j in range(max(h)):
        for i in range(n):
            if h[i] != 0 and h[i+1] == 0:
                count += 1
            if h[i] != 0:
                h[i] -= 1
    
    print(count)



if __name__ == '__main__':
    main()
