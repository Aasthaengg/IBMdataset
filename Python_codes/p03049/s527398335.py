N = int(input())
# N, K = [int(i) for i in input().split()]
countA = 0
countB = 0
countAB = 0
countBA = 0
for i in range(N):
    s = input()
    countAB += s.count('AB')
    if s[0] == 'B':
        countB += 1
    if s[-1] == 'A':
        countA += 1
    if s[0] == 'B' and s[-1] == 'A':
        countBA += 1
if countA != 0 and countA == countBA and countB == countBA:
    print(countAB + countBA - 1)
else:
    print(countAB + min(countA, countB))
