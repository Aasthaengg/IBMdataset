def main():
    n = int(input())
    # t, a = map(int, input().split())
    # h = list(map(int, input().split()))
    # s = input()

    p = []
    for i in range(n):
        p.append(int(input()))
    
    maxi = max(p)
    print(sum(p) - maxi//2)



if __name__ == '__main__':
    main()
