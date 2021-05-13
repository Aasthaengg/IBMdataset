k,t = map(int,input().split())
L = list(map(int,input().split()))

max1 = max(L)
zan = k-max1

print(max(0,(max1-1)-zan))