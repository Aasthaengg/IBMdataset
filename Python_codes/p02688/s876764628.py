n, k = map(int, input().split())

n_l = [1]*n

for i in range(k):
    a = int(input())
    for k in list(map(int, input().split())):
        n_l[k-1] = 0

print(sum(n_l))