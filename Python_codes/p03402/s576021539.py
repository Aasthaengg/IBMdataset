import sys
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))
MIIZ = lambda: list(map(lambda x: x-1, MII()))

def main():
    a, b = MII()
    grid=[['#' for i in range(100)] for j in range(50)]
    grid+=[['.' for i in range(100)] for j in range(50)]
    for i in range(a-1):
        grid[(i//50)*2][(i%50)*2]='.'
    for i in range(b-1):
        grid[(i//50)*2+51][(i%50)*2]='#'
    print(100,100)
    print(*[''.join(grid[i]) for i in range(100)], sep='\n')

if __name__ == '__main__':
    main()
