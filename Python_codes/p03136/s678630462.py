a=int(input())
b=list(map(int,input().split()))
if max(b)<(sum(b)-max(b)):
    print('Yes')
else:
    print('No')