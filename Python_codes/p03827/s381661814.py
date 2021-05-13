# B - Increment Decrement 
def main():
    n = int(input())
    s = input()
    cnt = 0
    ans = 0

    for i in range(n):
        if s[i] == 'I':
            cnt = cnt+1
            ans = max(cnt, ans)
        else:
            cnt = cnt-1
    else:
        print(ans)


if __name__ ==  "__main__":
    main()