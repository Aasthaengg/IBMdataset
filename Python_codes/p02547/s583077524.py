class Main:
    n = int(input())
    num_list =[]
    count = 0
    for i in range(n):
        num_list.append(list(map(int,input().split())))

    for i in range(n-2):
        if num_list[i][0]==num_list[i][1] and num_list[i+1][0]==num_list[i+1][1] and num_list[i+2][0]==num_list[i+2][1]:
            count +=1

    if count >= 1:
        print('Yes')
    else :
        print('No')