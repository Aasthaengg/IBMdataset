N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))
ans1 = 0
ans2 = 0
ans3 = 0  
for i in P:
    if A>=i:
        ans1 = ans1 + 1
    if A+1 <= i <= B:
        ans2 = ans2 + 1
    if B+1 <= i:
        ans3 = ans3 + 1 


print(min(ans1,ans2,ans3))
