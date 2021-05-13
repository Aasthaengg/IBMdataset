dd = list(map(int,input().split()))
nn = dd[0]
mm = dd[1]
cc = [int(input()) for i in range(nn)]
min_donut = min(cc)
residue = mm - sum(cc)
extra = int(residue / min_donut)
print(extra+nn)