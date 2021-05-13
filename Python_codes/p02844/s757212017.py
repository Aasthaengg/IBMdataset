def main():
    n = int(input())
    s = input()

    cnt = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                ii = s.find(str(i))
                if ii == -1:
                    continue
                jj = s[ii+1:].find(str(j))
                if jj == -1:
                    continue
                jj += ii+1
                kk = s[jj+1:].find(str(k))
                if kk == -1:
                    continue
                cnt += 1


    print(cnt)


main()