import re

N, A, B, C, D = map(int, input().split())
S = input()
S = '#' + S
flag = True
if re.search(r'##', S[min([A,B]): max([C,D])+1]):
    flag *= False

if D < C:
    if re.search(r'\.\.\.', S[B-1:D+2]):
        flag *= True
    else:
        flag *= False
        
print('Yes') if flag else print('No')