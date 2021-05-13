k, a, b = map(int, input().split())

if b-a <= 2 or k < a-1:
    print(k+1)

else:
    ans = ((k-(a-1))//2)*(b-a) + a +(k-(a-1))%2
    print(ans)