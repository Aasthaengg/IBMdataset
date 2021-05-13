h1,m1,h2,m2,k = map(int, input().split())

fin = h2 * 60 + m2

st = h1 * 60 + m1

ans = fin - st - k 

print(max(0,ans))