def main():
    n = list(input())
    ans = max(int(n[0])-1 + 9*(len(n)-1), int(n[0]), sum(map(int, n)))
    print(ans)

if __name__ == '__main__':
    main()    
