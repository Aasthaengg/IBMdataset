h, w = map(int, input().split())
board = [[i for i in input()] for _ in range(h)]

def check(i, j):
    if (j-1 >= 0):
        if(board[i][j-1] == "#"):
            return False
    if (j+1 < w):
        if(board[i][j+1] == "#"):
            return False
    if (i-1 >= 0):
        if(board[i-1][j] == "#"):
            return False
    if (i+1 < h):
        if(board[i+1][j] == "#"):
            return False

    return True

def main():
    for i in range(h):
        for j in range(w):
            if (board[i][j] == "#"):
                if(check(i,j)):
                    return "No"

    return "Yes"

if __name__ == '__main__':
    print(main())