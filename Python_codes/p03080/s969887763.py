def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
s = input()

if 2*s.count('R') > len(s):
    print('Yes')
else:
    print('No')