A = int(input())
listn = map(int,input().split())
listn = map(lambda x:x-1,listn)
print(sum(listn))