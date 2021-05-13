def main():
    N = int(input())
    buttons = {}
    for i in range(N):
        buttons.update({i+1:int(input())})
    # print(buttons)
    p = 1
    ans = 0
    while ans <= N:
        p = buttons[p]
        ans += 1
        if p == 2:
            print(ans)
            return
    print(-1)

if __name__ == '__main__':
    main()