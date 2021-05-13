import sys

#  Input
T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
runout = T1 * A1 - T1 * B1
TotalDiff = (T1 * A1 - T1 * B1) + (T2 * A2 - T2 * B2)

if TotalDiff == 0:
    print('infinity')
    sys.exit()
elif runout * TotalDiff > 0:
    print(0)
    sys.exit()

runout = abs(runout)
TotalDiff = abs(TotalDiff)

cnt = 0
cnt = (runout // TotalDiff) * 2
if runout % TotalDiff != 0:
    cnt += 1
print(cnt)
