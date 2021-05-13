

def main():
    s = input()
    n = len(s)
    cn = 0
    ans = 0
    for i in range(n):
        if s[i] == 'W':
            ans += (i - cn)
            cn += 1
    print(ans)



if __name__ == '__main__':
    main()
