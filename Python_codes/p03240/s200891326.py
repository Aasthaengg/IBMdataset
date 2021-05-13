def main():
    N = int(input())
    l = []
    for _ in range(N):
        x,y,h = map(int, input().split())
        l.append((x,y,h))
    l.sort(key=lambda x:x[2], reverse=True)
    for i in range(101):
        for j in range(101):
            H = l[0][2] +  abs(l[0][0] - i) + abs(l[0][1] - j)
            for k in range(N):
                if max(H-abs(l[k][0]-i) - abs(l[k][1] - j), 0) != l[k][2]:
                    break
            else:
                return i, j, H
i, j, H = main()
print(i,j,H)
