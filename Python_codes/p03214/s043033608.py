N, *A=map(int, open(0).read().split())
M=sum(A)/N
print(min((abs(M-a),i) for i,a in enumerate(A))[1])