k,t = map(int, input().split())
As = list(map(int, input().split()))

As.sort()
a = As[-1]
b = sum(As[:-1])

print(max(0,a-b-1))