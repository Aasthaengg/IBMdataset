def main():
 
    N, K = map(int, input().split())
    p = []
    for _ in range(N):
        x, y = map(int, input().split())
        p.append([x, y])
    p.sort(key = lambda x: x[0])
 
    min_area = float('inf')
    for i in range(N-1):
        for j in range(i+1, N):
            if j-i+1 >= K:
                x1 = p[i][0]
                x2 = p[j][0]
                ys = []
                for k in range(i, j+1):
                    ys.append(p[k][1])
                ys.sort()
                for k in range(len(ys)):
                    for l in range(k+K-1, len(ys)):
                        y1 = ys[k]
                        y2 = ys[l]
                        area = (x2-x1)*(y2-y1)
                        if area > 0:
                            min_area = min(min_area, area)
    return min_area
 
if __name__ == '__main__':
    print(main())