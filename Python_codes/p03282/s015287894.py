def main():
    s = input()
    k = int(input())

    m = 0
    ans = ""

    for i in range(len(s)):
        if s[i] != "1":
            m = i+1
            ans = s[i]
            break
    
    if k < m:
        print(1)
    elif m == 0:
        print(1)
    else:
        print(int(ans))



if __name__ == "__main__":
    main()