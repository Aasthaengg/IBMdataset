n = int(input())
kouho = [list(map(int,input().split())) for i in range(n)]
kouho = sorted(kouho,key=lambda x :x[2],reverse=True)

for cx in range(101):
    for cy in range(101):
        h = kouho[0][2] + abs(kouho[0][0]-cx) + abs(kouho[0][1]-cy)
        flag = False
        for i in range(1,n):
            now = max(h - abs(kouho[i][0]-cx) - abs(kouho[i][1]-cy),0)
            if now != kouho[i][2]:
                flag = True
                break
        if not flag:
            print(str(cx) + " " + str(cy) + " " + str(h))
            exit()