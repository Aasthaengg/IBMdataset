vals = [int(i) for i in input().split()]
s = vals[0]
w = vals[1]
res = ("safe" if(s > w) else "unsafe")
print(res)
