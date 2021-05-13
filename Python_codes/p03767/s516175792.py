n, *lst = map(int, open(0).read().split())
lst.sort(reverse=1)
print(sum(lst[1:1+2*n:2]))
