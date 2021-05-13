N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

transportations = [A, B, C, D, E]
minCap = min(transportations)
minIdx = transportations.index(minCap)
transportations.pop(minIdx)

time = N // minCap
if N % minCap != 0:
	time += 1
	
time += 4

print(time)
	
