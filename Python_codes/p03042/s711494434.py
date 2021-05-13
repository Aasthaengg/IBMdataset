S = input()
YYMM = 0
MMYY = 0
start = S[0:2]
end = S[2:4]
tmp1 = int(start)
tmp2 = int(end)
if(tmp2 <= 12 and tmp2 != 0):
    YYMM = 1
if(tmp1 <= 12 and tmp1 != 0):
    MMYY = 1
if(YYMM == 1 and MMYY == 1):
    print("AMBIGUOUS")
elif(YYMM == 1):
    print("YYMM")
elif(MMYY == 1):
    print("MMYY")
else:
    print("NA")