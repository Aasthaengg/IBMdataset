def main():
    s = input()
    x,y = map(int,input().split())

    x1 = []
    y1 = []
    cnt = 0
    cnt2 = 0

    for i in range(len(s)):
        s1 = s[i]
        if s1 == 'F':
            cnt += 1
        else:
            if cnt2 == 0:
                x -= cnt
            elif cnt2 % 2 == 0:
                x1.append(cnt)
            else:
                y1.append(cnt)
            cnt = 0
            cnt2 += 1

    if cnt2 == 0:
        x -= cnt

    if cnt > 0 and cnt2 > 0:
        if cnt2 % 2 == 0:
            x1.append(cnt)
        else:
            y1.append(cnt)

    if len(x1) == 0 and len(y1) == 0 and x == 0 and y == 0:
        print('Yes')
        exit()

    if sum(x1) < abs(x) or sum(y1) < abs(y):
        print('No')
        exit()

    dp1 = [[False] * (sum(x1)+1)*2 for _ in range((len(x1)+1))]
    dp2 = [[False] * (sum(y1)+1)*2 for _ in range((len(y1)+1))]
    dp1[0][sum(x1)+1] = True
    dp2[0][sum(y1)+1] = True

    for i in range(len(x1)):
        for j in range((sum(x1)+1)*2):
            if dp1[i][j]:
                dp1[i+1][j+x1[i]] = True
                dp1[i+1][j-x1[i]] = True

    for i in range(len(y1)):
        for j in range((sum(y1)+1)*2):
            if dp2[i][j]:
                dp2[i+1][j+y1[i]] = True
                dp2[i+1][j-y1[i]] = True

    if dp1[-1][sum(x1)+1+x] and dp2[-1][sum(y1)+1+y]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
