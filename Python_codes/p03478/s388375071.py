from functools import reduce

n,a,b = map(lambda x:int(x),input().split(" "))

ans = 0
for ni in range(a,n+1):
    if ni <= 9 :
        if a <= ni and ni <= b:
            ans += ni
    else:
        add_each_dig = reduce(lambda x, y: int(x) + int(y), str(ni) )
        if a <= add_each_dig and add_each_dig <= b:
            ans += ni

print(ans)