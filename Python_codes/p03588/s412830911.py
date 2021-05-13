n = int(input())
l = sorted([[int(i) for i in input().split()] for _ in range(n)],key = lambda x: x[0])

print(l[-1][0] + l[-1][1])

