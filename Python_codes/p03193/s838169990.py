n,h,w=map(int,input().split())
ab = []
for _ in range(n):
  ab.append(input().split())
  ab[-1][0] = int(ab[-1][0])
  ab[-1][1] = int(ab[-1][1])
  if ab[-1][0] < h or ab[-1][1] < w:
    ab.pop()
print(len(ab))