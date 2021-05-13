import re,sys
def S(): return sys.stdin.readline().rstrip()
S = S()
p1 = r'.*keyence'
p2 = r'k.*eyence'
p3 = r'ke.*yence'
p4 = r'key.*ence'
p5 = r'keye.*nce'
p6 = r'keyen.*ce'
p7 = r'keyenc.*e'
p8 = r'keyence.*'
if re.fullmatch(p1,S) or re.fullmatch(p2,S) or re.fullmatch(p3,S) or re.fullmatch(p4,S) or re.fullmatch(p5,S) or re.fullmatch(p6,S) or re.fullmatch(p7,S) or re.fullmatch(p8,S):
    print('YES')
else:
    print('NO')
