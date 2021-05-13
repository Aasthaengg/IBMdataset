def main():
    import numpy as np
    h,w = map(int,input().split())
    maize = []
    for i in range(h):
        s = input()
        maize.append(s)
    ans = 0
    for i in range(h):
        for j in range(w):
            que = [[i,j]]
            if maize[i][j] == '.':
                dis = [[-1 for i in range(w)] for i in range(h)]
                dis[i][j] = 0
                while len(que)>0:
                    q = que.pop(0)
                    if q[0]>0:
                        n = [q[0]-1,q[1]]
                        if maize[n[0]][n[1]]=='.':
                            if dis[n[0]][n[1]]==-1:
                                dis[n[0]][n[1]] = dis[q[0]][q[1]]+1
                                que.append(n)
                    if q[0] < h-1:
                        n = [q[0]+1,q[1]]
                        if maize[n[0]][n[1]]=='.':
                            if dis[n[0]][n[1]]==-1:
                                dis[n[0]][n[1]] = dis[q[0]][q[1]]+1
                                que.append(n)
                    if q[1] > 0:
                        n = [q[0],q[1]-1]
                        if maize[n[0]][n[1]]=='.':
                            if dis[n[0]][n[1]]==-1:
                                dis[n[0]][n[1]] = dis[q[0]][q[1]]+1
                                que.append(n)
                    if q[1] < w-1:
                        n = [q[0],q[1]+1]
                        if maize[n[0]][n[1]]=='.':
                            if dis[n[0]][n[1]]==-1:
                                dis[n[0]][n[1]] = dis[q[0]][q[1]]+1
                                que.append(n)
                dis = np.array(dis)
                if np.max(dis)>ans:
                    ans = np.max(dis)
    print(ans)
    

if __name__ == "__main__":
    main()
