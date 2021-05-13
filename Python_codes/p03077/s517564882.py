N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

L = [A, B, C, D, E]

minL = min(L)
print((N+minL-1)//minL + 4)