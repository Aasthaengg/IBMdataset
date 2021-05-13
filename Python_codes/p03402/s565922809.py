import sys
input = sys.stdin.readline
INF = 10**9
MOD = 10**9 + 7

def main():
    a,b = map(int,input().split())
    
    if a == 1 and b == 1:
        print(1,2)
        print('.#')
        exit()

    if a != 1:
        h1 = 2 * ((a - 2)//50 + 2) - 1
        lim1 = 1
        grid1 = [['#']*100 for _ in range(h1)]
    else:
        h1 = 0
        lim1 = 0

    if b != 1:
        h2 = 2 * ((b - 2)//50 + 1)
        lim2 = 1
        grid2 = [['.']*100 for _ in range(h2)]
    else:
        h2 = 0
        lim2 = 0
    
    i = 1
    j = 1
    while a > lim2:
        grid1[i][j] = '.'
        a -= 1
        j += 2
        if j == 101:
            i += 2
            j = 1
    
    i = 1
    j = 1
    while b > lim1:
        grid2[i][j] = '#'
        b -= 1
        j += 2
        if j == 101:
            i += 2
            j = 1

    print(h1 + h2, 100)

    for i in range(h1):
        print(''.join(grid1[i]))

    for i in range(h2):
        print(''.join(grid2[i]))

if __name__=='__main__':
    main()