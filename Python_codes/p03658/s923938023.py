i = list(map(int, input().split()))
N = i[0]
K = i[1]
l = list(map(int, input().split()))

l.sort(reverse=True)
l = l[0:K]
print(sum(l))