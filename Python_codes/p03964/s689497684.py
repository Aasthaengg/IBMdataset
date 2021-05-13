import sys

def read():
	return tuple([int(d) for d in sys.stdin.readline().rstrip().split(" ")])

N, = read()

cur_T = 1
cur_A = 1

for i in range(N):
	T, A = read()

	current = cur_T + cur_A
	sum = T + A

	mult1 = (current + sum - 1) // sum
	mult2 = (cur_T + T - 1) // T
	mult3 = (cur_A + A - 1) // A

	mult = mult1
	if mult2 > mult: mult = mult2
	if mult3 > mult: mult = mult3

	cur_T = T * mult
	cur_A = A * mult

print(cur_T + cur_A)
