nim,mike = map(int,input().split())

data = int(input())

array = list(map(int,input().split()))

ans = []
for i,v in enumerate(array):
    ans += [i+1] * v
for i in range(nim):
    print(*ans[mike * i:mike*(i+1)][::(-1)**i])
