N = int(input())
A = []
for i in range(N):
  S,P = map(str,input().split())
  List = [S,int(P),i+1]
  A.append(List)

sorted_data = sorted(A, key=lambda x:(x[0], -x[1]))

for i in range(len(sorted_data)):
  print(sorted_data[i][2])