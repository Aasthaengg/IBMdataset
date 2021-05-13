n = int(input())
a = list(map(int, input().split()))

b = [i for i in range(1, n+1)]

d = dict(zip(a,b))

sorted_d = sorted(d.items(), key=lambda x:x[0])

print(' '.join([str(sorted_d[i][1]) for i in range(n)]))