n=int(input())
ab=[list(map(int,input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
print(ab[-1][0]+ab[-1][1])