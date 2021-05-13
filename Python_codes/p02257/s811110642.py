print(sum(map(lambda x: 1 if x == 2 or pow(2,x-1,x) == 1 else 0, [int(input()) for _ in range(int(input()))])))
