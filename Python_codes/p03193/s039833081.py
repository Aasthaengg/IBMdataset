nhw = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(nhw[0])]
ab.sort(reverse=True)
aba = [i for i in ab if i[0] >= nhw[1]]
abab = [i for i in aba if i[1] >= nhw[2]]
print(len(abab))
