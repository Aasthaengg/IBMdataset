import sys
S = str(input())
K = int(input())

if len(S) == 1:
    print(S[0])
    sys.exit()

count = 0
l = 0
for i in range(len(S)):
    if S[i] == '1':
        count += 1
    else:
        break
#print(count)
    
if count < K:
    print(S[count])
else:
    print(1)