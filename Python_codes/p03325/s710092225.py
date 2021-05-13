def main():
    num = int(input())
    x_list = list(map(int, input().split()))
    ans = 0

    for i in range(num):
        x = x_list[i]
        while  x%2 == 0:
            ans += 1
            x = x//2

    print(ans)

    
if __name__ == '__main__':
    main()