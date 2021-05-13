A,B,C,X = map(int,open(0).read().split())
print(sum(500*a+100*b+50*c==X for a in range(A+1) for b in range(B+1) for c in range(C+1)))