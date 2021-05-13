from sys import stdin
N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [int(x) for x in stdin.readline().rstrip().split()]

cnt1 = 0 
cnt2 = 0

for i in range(N):
    if A[i] > B[i]:
        cnt1 += (A[i] - B[i])
    else:
        cnt2 += ((B[i]-A[i])//2)
        
if cnt1 <= cnt2:
    print("Yes")
else:
    print("No")