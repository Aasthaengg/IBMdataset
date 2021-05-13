n = int(input())
B = [[0 for i in range(n)] for j in range(n)]
chk = [0 for i in range(n)]
s = []
i_array = [0 for i in range(n)]
time = 1
node_start_time = [0 for i in range(n)]
node_finish_time = [0 for i in range(n)]

for i in range(n):
    A = list(map(int,input().split()))
    for j in range(A[1]):
        B[A[0]-1][A[j+2]-1] = 1

for i in range(n):
    if(chk[i] == 1):
        continue
    chk[i] = 1
    node_start_time[i] = time
    time += 1
    s.append(i)
    while(len(s) != 0):
        flag = 0
        v = s[len(s)-1]
        for j in range(i_array[v],n):
            if(B[v][j] == 1 and chk[j] == 0):
                chk[j] = 1
                s.append(j)
                node_start_time[j] = time
                time += 1
                i_array[v] = j+1
                flag = 1
                break
        if(flag == 0):
            s.pop()
            node_finish_time[v] = time
            time += 1

for i in range(n):
    print(i+1,node_start_time[i],node_finish_time[i])
