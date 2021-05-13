def resolve():
    n = int(input())
    lists = list(map(int, input().split()))
    count = 0
    for i in range(1,n-1):
        if lists[i-1] < lists[i] < lists[i+1] or lists[i-1] > lists[i] > lists[i+1]:
            count += 1
    print(count)
resolve()