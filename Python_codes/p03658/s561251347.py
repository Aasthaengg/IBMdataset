N,K = map(int,input().split())
# print(N,K)
l = list(map(int,input().split()))
# print(l)

l_sort = sorted(l, reverse=True)

# print(l_sort)
a =0
for i in range(K):
    a += l_sort[i]
print(a)
