n = int(input())
a = list(map(lambda x:int(x)%2,input().split()))
if sum(a)%2 == 0:
    print("YES")
else:
    print("NO")