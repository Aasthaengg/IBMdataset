if __name__=="__main__":
    N = int(input())
    l = list(map(int,input().split(" ")))
    record = []
    dic = {i:l[i] for i in range(N)}
    sorted_list = sorted(dic.items(),key=lambda d:d[1],reverse=True)
    if sorted_list[N-1][1]>=0:
        for i in range(N-1):
            record.append([i, i+1])
    elif sorted_list[0][1]<0:
        for i in range(N-1,0,-1):
            record.append([i, i-1])
    elif sorted_list[0][1]+sorted_list[N-1][1]>=0:
        record.append([sorted_list[0][0], 0])
        record.append([sorted_list[0][0], 1])
        record.append([0,1])
        for i in range(1,N-1):
            record.append([sorted_list[0][0], i+1])
            record.append([i,i+1])
    elif sorted_list[0][1]+sorted_list[N-1][1]<0:
        record.append([sorted_list[N-1][0], N-1])
        record.append([sorted_list[N-1][0], N-2])
        record.append([N-1,N-2])
        for i in range(N-2,0,-1):
            record.append([sorted_list[N-1][0], i-1])
            record.append([i,i-1])
    print(len(record))
    for i in range(len(record)):
         print(str(record[i][0]+1)+" "+str(record[i][1]+1))