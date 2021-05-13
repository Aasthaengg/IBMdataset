A = [int(input()) for n in range(5)]
B = [(a+9)//10*10 for a in A]
C = sum(B)
print(min([C-B[n]+A[n] for n in range(5)]))