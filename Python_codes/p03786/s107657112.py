N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

import itertools
Ruisekiwa = list(itertools.accumulate(A))

count = 1

Dekiru = [0]*N
Dekiru[N-1] = 1

for i in range (1, N):
	if 2*Ruisekiwa[N-i-1] >= A[N-i] and Dekiru[N-i] == 1:
		count+=1
		Dekiru[N-i-1]=1
        
print(count)