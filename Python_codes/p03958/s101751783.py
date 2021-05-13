K, T = map(int, input().split())
alist = sorted(list(map(int, input().split())))[::-1]
alist.append(0)
print(max(0, alist[0]-sum(alist[1:])-1))