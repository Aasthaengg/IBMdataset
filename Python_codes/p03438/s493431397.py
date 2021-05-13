n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

m = sum(B)-sum(A)
cnt1 = 0
cnt2 = 0
for a, b in zip(A, B):
    if a > b:
        cnt1 += (a-b)
    elif a < b:
        cnt2 += (b-a+1)//2
    else:
        pass

if cnt1 <= m and cnt2 <= m:
    print('Yes')
else:
    print('No')
