input();A=list(map(int,input().split()));b,B=A[0],[];
for i in range(1,len(A)):
  b=min(b,A[i]);B.append(A[i]-b);
print(B.count(max(B)))