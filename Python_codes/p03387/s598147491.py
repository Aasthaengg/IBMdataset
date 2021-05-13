A,B,C=map(int, input().split())
m = max([A,B,C])
s = sum([m-A, m-B, m-C])
if s %2 == 0:
    print(s//2)
else:
    s += 1
    print(1+s//2)