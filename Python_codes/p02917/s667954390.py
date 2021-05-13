n = int(input())
list_B = list(map(int, input().split()))
list_A = [list_B[0]]
for i in range(len(list_B)-1):
  list_A.append(min(list_B[i], list_B[i+1]))
list_A.append(list_B[-1])
print(sum(list_A))