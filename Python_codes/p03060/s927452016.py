n = int(input())
vn = [int(num) for num in input().split()]
cn = [int(num) for num in input().split()]

answer = 0
for i in range(n):
  if (vn[i] - cn[i]) > 0:
    answer += vn[i] - cn[i]
    
print(answer)