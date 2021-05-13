n =int(input())
s = []
for i in range(n):
    l,r = map(int,input().split())
    s += [r-l+1]
print(sum(s))
    




