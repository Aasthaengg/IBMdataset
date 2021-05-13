n = int(input())
a = sum(list(map(lambda x:1-int(x)%2,input().split())))
print(3**n-2**a)
