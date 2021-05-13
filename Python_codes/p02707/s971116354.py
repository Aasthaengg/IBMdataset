N = int(input())
A = list(map(int,input().split()))
B = N*[0]

for a in A:
  B[a-1]+=1

print(*B,sep="\n")