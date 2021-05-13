N = int(input())
S = input()

x = 0
A = [0]
for i in range(N):
	if S[i] == "I":
		x += 1
		A.append(x)
	else:
		x += -1
		A.append(x)
#print(A)
print(max(A))