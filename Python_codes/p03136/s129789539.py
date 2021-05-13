N = int(input())
L = list(map(int,input().split()))
maxLength = max(L)
sumOtherLength = sum(L) - maxLength
if maxLength < sumOtherLength:
    print("Yes")
else:
    print("No")