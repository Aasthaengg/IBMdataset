def main():
    s = input()
    t = s[::-1]
    ans = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            ans += 1
    print(ans//2)


    
    
if __name__ == "__main__":
    main()
