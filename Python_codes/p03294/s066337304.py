def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    maximum = sum(a_lst) - n
    
    print(maximum)
    

if __name__ == '__main__':
    main()