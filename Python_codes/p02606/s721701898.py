A,B,C = map(int,input().split())
num_list = []
for i in range(A,B+1):
  if i % C == 0:
    num_list.append(i)

print(len(num_list))