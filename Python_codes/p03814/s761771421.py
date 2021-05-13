sn = input()
r_sn = list(reversed(sn))
print(len(sn[sn.index("A"):len(sn)-r_sn.index("Z")]))