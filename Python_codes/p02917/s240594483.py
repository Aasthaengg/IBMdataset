N = int(input())
B = input().split(' ')
B = [int(B[i]) for i in range(N-1)]
SUM = [B[0], B[-1]]
for i in range(N-2):
  if B[i]>=B[i+1]:
    SUM.append(B[i+1])
  else:
    SUM.append(B[i])
print(sum(SUM))