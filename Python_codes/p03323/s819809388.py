import sys
input = sys.stdin.readline
A,B = [int(i) for i in input().split()]
ans = "Yay!"
if A > 8 or B > 8 :
    ans = ":("
print(ans)