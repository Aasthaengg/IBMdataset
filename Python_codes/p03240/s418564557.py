import sys
n = int(input())
inf_ls = [[0]*3 for _ in range(n)]
for i in range(n):
    x,y,h = map(int,input().split())
    inf_ls[i] = x,y,h
for Cx in range(101):
    for Cy in range(101):
        this_is_C = True
        H_set = set()
        zero_ls = []
        for i in range(n):
            x,y,h = inf_ls[i]
            if h > 0:
                H = abs(x-Cx) + abs(y-Cy) + h
                H_set.add(H)
            else:
                zero_ls.append([x,y])
        if len(H_set) != 1:
            this_is_C = False
            continue
        H = list(H_set)[0]
        for x,y in zero_ls:
            if H - abs(x-Cx) - abs(y-Cy) > 0:
                this_is_C = False
        if this_is_C:
            print(Cx,Cy,H)
            exit()



