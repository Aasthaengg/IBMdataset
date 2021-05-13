S = input()
n = len(S)
A = [0] * n
p = 0
for i in range(n-1):
    if S[i] == 'R' and S[i+1] == 'L':
        for j in range(p, i+1):
            if S[j] == 'R':
                if (i+1-j)%2==0:
                    A[i+1]+=1
                else:
                    A[i]+=1
        p = i + 1
p = n - 1
for i in range(n-1, 0, -1):
    if S[i-1] == 'R' and S[i] == 'L':
        for j in range(p, i-1, -1):
            if S[j] == 'L':
                if (i-1-j)%2==0:
                    A[i-1]+=1
                else:
                    A[i]+=1
        p = i - 1
print(*A)
