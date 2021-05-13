n,m = map(int,input().split())

k_lst = []
a_lst = []
for _ in range(n):
    lst = list(map(int,input().split()))
    k_lst.append(lst[0])
    a_lst.append(lst[1:])

temp = a_lst[0]

for i in range(1,n):
    lstwa = temp + a_lst[i]
    tyofuku = [x for x in set(lstwa) if lstwa.count(x) > 1]
    temp = tyofuku

print(len(temp))