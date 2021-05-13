def main():
    n = int(input())
    xyh = [list(map(int, input().split())) for _ in range(n)]
    xyh.sort(key = lambda x:x[2], reverse = True)
    x_ = xyh[0][0]
    y_ = xyh[0][1]
    h_ = xyh[0][2]
    for i in range(101):
        for j in range(101):
            top = h_ + abs(i - x_) + abs(j - y_)
            for x, y, h in xyh[1:]:
                h_2 = top - abs(i - x) - abs(j - y)
                if h != max(h_2, 0):
                    break
            else:
                print(i, j, top)
                return
                
main()