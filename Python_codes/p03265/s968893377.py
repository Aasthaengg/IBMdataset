def solve():
    x1,y1, x2,y2 = map(int, input().split())
    a = x2-x1
    b = y2-y1
    print(x2-b, y2+a, x2-b-a,y2+a-b)



if __name__ == '__main__':
    solve()