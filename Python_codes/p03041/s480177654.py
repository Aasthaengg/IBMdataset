import sys
import re
N,K = map(int,input().split())
S = input()

if not ( 1 <= N <= 50 and 1 <= K <= N ): sys.exit()
if len(re.findall(r'[^(A|B|C)]',S)) != 0 : print("NG");sys.exit()

res = []
for I in range(len(list(S))):
    res.append(S[I]) if I + 1 != K else res.append(S[I].lower())
print(''.join(res))