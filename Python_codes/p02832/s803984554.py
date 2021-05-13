def main():
    N = int(input())
    a = list(map(int, input().split()))

    if a.count(1) == 0:
        print(-1)
        return
    index = 1
    cnt = 0
    for i in range(N):
        if index == a[i]:
            index+=1
        else:
            cnt+=1

    print(cnt)






if __name__ == '__main__':
    main()