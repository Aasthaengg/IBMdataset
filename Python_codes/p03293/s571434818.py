import sys
input = sys.stdin.readline
 
S = input().rstrip('\n')
T = input().rstrip('\n')

result = 'No'

for i in range(len(S)):
  if S[-i:]+S[:-i] == T:
    result ='Yes'

      
print(result)
