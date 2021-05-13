h1,w1 = list(map(int,input().split()))
h2,w2 = list(map(int,input().split()))

ans = h1*w1 - h2*w1 - h1*w2 + h2*w2
print(ans)
