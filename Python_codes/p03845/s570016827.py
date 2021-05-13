import copy

n = int(input())
lis = list(map(int, input().split()))

m = int(input())
for i in range(m):
    tmp = copy.deepcopy(lis)
    a, b = map(int, input().split())
    tmp[a-1] = b
    print(sum(tmp))
