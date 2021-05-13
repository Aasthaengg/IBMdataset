n = int(input())
l = [int(input()) for _ in range(n)]
cou = [0 for i in range(n+1)]
for i in l:
  cou[i] = cou[i-1]+ 1
print(n-max(cou))