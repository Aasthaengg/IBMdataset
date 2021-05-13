def inN():
    return int(input())
def inL():
    return list(map(int,input().split()))
def inNL(n):
    return [list(map(int,input().split())) for i in range(n)]
k = inN()
s = input()
l = len(s)
if k >= l:
    print(s)
else:
    print(s[:k]+"...")