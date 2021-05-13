def main():
    n, k = map(int, input().split())
    p_lst = list(map(int, input().split()))
    p_lst.sort()
    minimum = 0
    
    for i in range(k):
        price = p_lst[i]
        minimum += price
        
    print(minimum)
    

if __name__ == '__main__':
    main()