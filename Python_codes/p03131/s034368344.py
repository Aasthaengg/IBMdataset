k,a,b = list(map(int, input().split()))

# 2手かけて増えるのが2枚以下なら地道に増やす
if b-a <= 2:
    print(1+k)
else:
    k -= a-1
    q,r = divmod(k,2)
    print(a+q*(b-a)+r)