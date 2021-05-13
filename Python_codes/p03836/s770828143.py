SX, SY, TX, TY = map(int, input().split())

TX -= SX
TY -= SY
SX = 0
SY = 0

res = ""

res += "U"*TY
res += "R"*TX
res += "D"*TY
res += "L"*(TX+1)
res += "U"*(TY+1)
res += "R"*(TX+1)
res += "D"
res += "R"
res += "D"*(TY+1)
res += "L"*(TX+1)
res += "U"

print(res)