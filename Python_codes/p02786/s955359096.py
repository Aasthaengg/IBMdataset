def main4():
    n = int(input())
    m=1
    cnt = 0
    while(n>0):
        cnt += m
        n//=2
        m *= 2
    print(cnt)

if __name__ == '__main__':
    main4()
