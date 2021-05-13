a,b = map(int,input().split())
c = list(map(int,input().split()))
c.sort(reverse = True)
print(sum(c[:b]))