import sys
S = input()
if S == 'level':
    print('No')
    sys.exit()


for i in range((len(S)//2)-1):
    if S[i] != S[len(S)-1-i]:
        print('No')
        sys.exit()
       
for j in range((len(S)//4)-1):
    if S[j] != S[(len(S)//2)-j-1]:
        print('No')
        sys.exit()

for k in range((len(S)//4)-1):
    if S[(len(S)//2)+1+k] != S[len(S)-k-1]:
        print('No')
        sys.exit()

print('Yes')