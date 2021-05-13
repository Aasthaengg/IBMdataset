n = int(input())
T = [0]*n
A = [0]*n

for i in range(n):
    T[i],A[i] = map(int,input().split())

votes = [T[0],A[0]]

for i in range(1,n):
    m = max(-(-votes[0]//T[i]),-(-votes[1]//A[i]))
    votes[0] = m*T[i]
    votes[1] = m*A[i]

print(votes[0]+votes[1])

#floatで正確に表示できるのは15桁程度