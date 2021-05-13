A = list(map(int,input().split()))
B = str(sorted(A)[-1])
C = str(sorted(A)[-2])
print(int(B+C)+min(A))