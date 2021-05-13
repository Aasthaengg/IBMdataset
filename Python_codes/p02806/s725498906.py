N = int(input())
jisyo = {}
for i in range(N):
  AA = input().split()
  jisyo[AA[0]] = AA[1]
SS = input()
count = 0
total = 0
for i,j in jisyo.items():
  if count == 1:
    total += int(j)
  if i == SS:
    count = 1
print(total)