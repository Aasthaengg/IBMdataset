P,Q,R = map(int, input().split())

ABC = P+Q
ACB = R+Q
BAC = P+R
BCA = Q+R
CAB = R+P
CBA = Q+P

print(min(ABC,ACB,BAC,BCA,CAB,CBA))