if __name__ == '__main__':
    n, m = map(int, input().split())
    likeList =[0]*m
    for i in range(n):
        a = [int(i) for i in input().split()]
        for j in range(1,a[0]+1):
            likeList[a[j]-1]+=1


    count =0
    for i in likeList:
        if n == i:
            count+=1
    print(count)