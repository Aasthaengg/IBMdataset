s = str(input())
n = len(s)
D = [0]*3
for i in range(n):
    D[ord(s[i])-ord('a')] += 1
#print(D)

D.sort(reverse=True)

if D[0]-1 <= D[1] <= D[0] and D[2] >= D[0]-1:
    print('YES')
else:
    print('NO')
