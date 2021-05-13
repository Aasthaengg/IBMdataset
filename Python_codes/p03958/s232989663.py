
K,T = list(map(int, input().split()))
As = list(map(int, input().split()))

goods = K - max(As)
ans = K - goods * 2

if ans <= 0:
    print(0)
else:
    print(ans-1)


