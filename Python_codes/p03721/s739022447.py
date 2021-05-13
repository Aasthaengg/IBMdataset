def main4():
    lis = []
    n,k=map(int, input().split())
    for i in range(n):
        a,b = map(int, input().split())
        lis.append([a,b])
    lis.sort(key = lambda x:x[0])
    res = 0
    i=-1
    while(res < k):
        i+=1
        res += lis[i][1]
        if(res>=k):
            print(lis[i][0])
            break


if __name__ == '__main__':
    main4()
