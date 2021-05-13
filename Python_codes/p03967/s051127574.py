def main():
    s = input()
    n = len(s)
    ans = 0
    g,p = 1,0
    for i in range(1,n):
        if g>p:
            if s[i]=='g':
                ans += 1
            p+=1
        else:
            if s[i]=='p':
                ans -=1
            g += 1
    print(ans)
            

if __name__ == "__main__":
    main()
