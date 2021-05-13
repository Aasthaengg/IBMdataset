N,K = map(int, input().split())
l = list(map(int,input().split()))
l.sort()
lrev = l[::-1]
print(sum(lrev[:K]))
