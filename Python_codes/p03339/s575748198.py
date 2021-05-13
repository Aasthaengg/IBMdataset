N = int(input())
S = input()

left = 0
right = S[1:].count('E')

cnt = [left+right]

for i in range(1,len(S)):
    if S[i-1] == 'W':
        left += 1
    
    if S[i] == 'E':
        right -= 1
        
    cnt.append(left+right)

print(min(cnt))