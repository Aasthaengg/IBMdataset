n = int(input())
d = list(map(int, input().split()))

d = sorted(d)

print(d[(n-1)//2+1]-d[(n-1)//2])
