def main():
    n = int(input())
    # 奇数の数
    m = n - (n // 2)
    ans = m / n
    print(ans)
    
if __name__ == '__main__':
    main()