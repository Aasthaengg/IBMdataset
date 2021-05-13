import sys
input = sys.stdin.readline
import bisect

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort();B.sort();C.sort()
#print(A)
#print(B)
#print(C)
Bok = []
for b in B:
  temp = bisect.bisect_left(A,b) #1indexでの位置
  Bok.append(temp) #個数なのでindexで持つ
SB = [0]
for i in range(N):
  temp = SB[-1]+Bok[i]
  SB.append(temp)
#print(SB)
ans = 0
for c in C:
  temp = bisect.bisect_left(B,c) #1indexでの位置
  #print(temp,SB[temp])
  ans += SB[temp]
print(ans)