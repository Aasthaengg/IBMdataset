N = int(input())
d = [int(x) for x in input().split()]
dd = sorted(d)

t=N//2
print(dd[t]-dd[t-1])
    
