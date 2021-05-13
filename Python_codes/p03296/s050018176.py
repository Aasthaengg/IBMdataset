from itertools import groupby

def main():
    N = int(input())
    a = list(map(int,input().split()))
    gp = []
    for key,value in groupby(a):
        gp.append(list(value))
    ans = 0
    for i in range(len(gp)):
        ans += len(gp[i])//2
    print(ans)

if __name__ == '__main__':
    main()