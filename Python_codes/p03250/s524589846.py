A,B,C=input().split()
print(max(int(A+B)+int(C),int(A+C)+int(B),int(B+A)+int(C),int(C+A)+int(B),int(B+C)+int(A),int(C+B)+int(A)))
