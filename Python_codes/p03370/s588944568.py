n, x = list(map(int, input().split())) 
mList = [int(input()) for _ in range(n)]
print((x-sum(mList)) // min(mList) + len(mList))
