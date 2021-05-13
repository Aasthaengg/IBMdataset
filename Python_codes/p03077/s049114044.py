import math
N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
m = max(math.ceil(N/A),math.ceil(N/B),math.ceil(N/C),math.ceil(N/D),math.ceil(N/E))
print(m+4)