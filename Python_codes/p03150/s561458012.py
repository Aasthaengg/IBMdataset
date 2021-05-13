# Q2
S=str(input())
#print(S)

K='keyence'
#print(len('keyence'))
ans=0

'''
print('first=',S[0:6])
print('last=',S[len(S)-7:])
if S[0:7]==K:
    ans=1
if S[len(S)-7:]==K:
    ans=1
'''

for i in range(7+1):
#    print(S[0:i]+S[len(S)-7+i:])
    if S[0:i]+S[len(S)-7+i:]==K:
        ans=1

        
if ans==1:    
    print('YES')
else:
    print('NO')
