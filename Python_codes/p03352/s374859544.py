x = int(input())
A = [a**b for a in range(1, 35) for b in range(2, 10) if a**b <= x]
A.sort()
print(A[-1])