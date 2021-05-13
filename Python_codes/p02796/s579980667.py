if __name__ == "__main__":
    N=int(input())
    robot=[]
    cnt=0
    last = -1e9
    for _ in range(N):
        x, l = map(int,input().split())
        robot.append((x - l, x+l))
    robot.sort(key=lambda x: x[1])
    for i in range(N):
        if last <=robot[i][0]:
            cnt+=1
            last = robot[i][1]
    print(cnt)
