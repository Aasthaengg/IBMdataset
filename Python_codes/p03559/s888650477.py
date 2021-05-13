n = int(input())
an = sorted([int(i) for i in input().split()])
bn = sorted([0]+[int(i) for i in input().split()])
cn = sorted([int(i) for i in input().split()])
dpb = [0]*(n+1)
dpc = [0]*n
cnt = 0
for i in range(n+1):
  while cnt < n and bn[i] > an[cnt]:
    cnt += 1
  dpb[i] = cnt
cnt = 0
temp = 0
for i in range(n):
  while cnt < n+1 and cn[i] > bn[cnt]:
    temp += dpb[cnt]
    cnt += 1
  dpc[i] = temp
print(sum(dpc))