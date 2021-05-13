import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for ia in range(A+1):
    for ib in range(B+1):
        for ic in range(C+1):
            if 500*ia+100*ib+50*ic == X:
                ans +=1
print(ans)
