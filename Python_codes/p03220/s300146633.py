n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
y = list(map(lambda x:abs((t-(x*0.006)) - a), h))
print(y.index(min(y))+1)