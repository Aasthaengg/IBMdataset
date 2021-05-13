X = int(input())
ASSET = 100
cnt = 0

while ASSET < X:
  tmp = str(ASSET)
  ASSET += int(tmp[:len(tmp)-2])
  cnt += 1

print(cnt)
