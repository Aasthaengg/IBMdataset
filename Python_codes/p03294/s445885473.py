n = int(input())
ls = list(map(int,input().split()))
y = lambda x : x-1
print(sum(list(map(y,ls))))