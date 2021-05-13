ab=[list(map(int, input().split())) for i in range(int(input()))]
ab.sort(reverse=True, key=lambda x:x[0]+x[1])
print(sum(map(lambda x:x[0],ab[::2]))-sum(map(lambda x:x[1],ab[1::2])))