N,K = map(int,input().split())

command = [list(map(int,input().split())) for i in range(N)]

command.sort()

ind = 0
for i in range(N):
    if ind + command[i][1]>=K:
        print(command[i][0])
        exit()
    else:
        ind += command[i][1]
