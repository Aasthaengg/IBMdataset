def main():
    input_string = list(map(int,input().split()))
    N = input_string[0]
    C = input_string[1]
    data = []
    max_time = 0
    for i in range(N):
        data.append(list(map(int,input().split())))
        max_num = max(data[i])
        if max_num>max_time:
            max_time=max_num

    #data_np = np.array(data).reshape(N,3)
    #data_np = np.array(data)

    #max_time = int(max(data))
    #print("max",max_time)
    schedule = [[0]*C for i in range(max_time)]
    #schedule = np.zeros([max_time,C])

    for i in range(N):
        start = data[i][0]-1
        end = data[i][1]-1
        channel = data[i][2]-1
        for j in range(end-start+1):
            if start+j-1<0:continue
            schedule[start+j-1][channel] = 1

#    for c in range(C):
#        for t in range(max_time):
#            if t==0:continue
#            if schedule[t][c]==1 and schedule[t-1][c]==0:
#                schedule[t-1][c]=1

    #max_N =0
    #for t in range(max_time):
    #    sum_of_ch = sum(schedule[t])

    temp = list(map(sum,list(schedule)))
    max_N = int(max(temp))


    #    if sum_of_ch>max_N:
    #        max_N = int(sum_of_ch)
    print(max_N)







main()
