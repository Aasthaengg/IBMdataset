def inN():
    return int(input())
def inL():
    return list(map(int,input().split()))
def inNL(n):
    return [list(map(int,input().split())) for i in range(n)]
s = input()
t = input()
if s == t[:-1]:
    print("Yes")
else:
    print("No")