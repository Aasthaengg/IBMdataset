x,y = input().split()
d = {"1":300000,"2":200000,"3":100000}
if x=="1" and y=="1":
    print(d.get(x,0)+d.get(y,0)+400000)
else:
    print(d.get(x,0)+d.get(y,0))
