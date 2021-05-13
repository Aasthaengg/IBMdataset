n, t = map(int,input().split())
A = list(map(int,input().split()))

dict = {"tmpmin":A[0],"maxvalue":0,"pairs":0}
for i in range(1,n):
    if A[i] < dict["tmpmin"]:
        dict["tmpmin"] = A[i]
    else:
        if A[i] - dict["tmpmin"] > dict["maxvalue"]:
            dict["maxvalue"] = A[i] - dict["tmpmin"]
            dict["pairs"] = 1
        elif A[i] - dict["tmpmin"] == dict["maxvalue"]:
            dict["pairs"] += 1
print(dict["pairs"])
