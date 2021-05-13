while True:
    try:
        n = int(input())
        S = list(map(int, input().split()))
        _ = int(input())
        print(sum([1 for t in list(map(int, input().split())) if t in S]))
    except:break