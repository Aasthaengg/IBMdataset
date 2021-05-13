import sys
S = list(map(int,input()))

if len(S) != 4: sys.exit()

if 1 <= int(str(S[0])+str(S[1])) <= 12 and 1 <= int(str(S[2])+str(S[3])) <= 12: print('AMBIGUOUS');sys.exit()
if int(str(S[0])+str(S[1])) >= 13 and 1 <= int(str(S[2])+str(S[3])) <= 12: print('YYMM');sys.exit()
if 0 == int(str(S[0])+str(S[1])) and 1 <= int(str(S[2])+str(S[3])) <= 12: print('YYMM');sys.exit()
if 1 <= int(str(S[0])+str(S[1])) <= 12 and 13 <= int(str(S[2])+str(S[3])): print('MMYY');sys.exit()
if 1 <= int(str(S[0])+str(S[1])) <= 12 and 0 == int(str(S[2])+str(S[3])): print('MMYY');sys.exit()
print('NA')