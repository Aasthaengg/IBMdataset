def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b,c,d = iim()

if abs(a-c) <= d or (abs(a-b) <= d and abs(b-c) <= d):
    print('Yes')
else:
    print('No')