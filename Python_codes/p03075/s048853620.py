def main():
    a_list = [int(input()) for i in range(5)]
    k = int(input())
    
    ans = "Yay!"
    
    if a_list[4] - a_list[0] > k:
        ans = ":("
    
    print(ans)


if __name__ == '__main__':
    main()

