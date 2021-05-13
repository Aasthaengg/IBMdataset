K,T = list(map(int, input().split()))
a = list(map(int, input().split()))

m = max(a)
o = sum(a)-m

print(max(m-o-1, 0))