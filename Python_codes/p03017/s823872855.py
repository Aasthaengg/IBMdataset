def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n,a,b,c,d = iim()
s = input()
st = s[b-2:min(c,d)+1]
s = s[a-1:max(c,d)]

if '##' in s:
    print('No')
elif c < d:
    print('Yes')
else:
    print('Yes' if '...' in st else ' No')