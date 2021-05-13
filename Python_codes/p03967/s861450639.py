S = input()
pd = len(S) // 2
gd = len(S) - pd
pt = S.count("p")
gt = len(S) - pt

score = min(pd,gt) - min(pt,gd)
print(score)