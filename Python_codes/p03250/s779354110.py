a,b,c = map(int, input().split())
l = [a,b,c]
l = sorted(l)
print(l[-1]*10 + l[-2] + l[-3])