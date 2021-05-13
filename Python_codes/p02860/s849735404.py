def main():
    n = int(input())
    s = input()
    tmp = 0
    if n%2 != 0:
        print("No")
        exit()
    for i in range(n//2):
        if s[i] != s[int(n/2)+i]:
            tmp += 1
    if tmp > 0:
        print('No')
    else:
        print('Yes')


    
    
if __name__ == "__main__":
    main()
