n, k, q = list(map(int, input().split()))

ns_points = [k] * n
ns_corrects = [0] * n
for i in range(q):
    ns_corrects[int(input())-1] += 1


for j in range(len(ns_points)):
    if ns_points[j] - (q - ns_corrects[j]) <= 0:
        print('No')
    else:
        print('Yes')