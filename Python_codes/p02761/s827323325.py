def main():
    n, m = map(int, input().split())
    ans = [0]*n
    flag = False

    if m == 0:
        if n > 1:
            ans[0] = 1
            print(''.join(map(str, ans)))
            return 0
        
        print(''.join(map(str, ans)))
        return 0

    s_c = []
    for i in range(m):
        temp_s, temp_c = map(int, input().split())
        s_c.append([temp_s, temp_c])
        ans[temp_s-1] = temp_c

    for i, j in s_c:
        if not(ans[i-1] == j) or (i-1 == 0 and j == 0 and n > 1):
            flag = True
            break

    if flag:
        print(-1)
    else:
        if ans[0] == 0 and n > 1:
            ans[0] = 1
        
        print(''.join(map(str, ans)))
        


if __name__ == '__main__':
    main()