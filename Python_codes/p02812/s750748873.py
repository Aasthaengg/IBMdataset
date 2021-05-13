N = int(input())
S = input()
count = 0
if N == 3:
  if S == 'ABC':
    count = 1
elif N > 3:
	for i in range(N-2):
		if S[i] == 'A':
			if S[i+1] == 'B':
				if S[i+2] == 'C':
					count += 1
print(count)
