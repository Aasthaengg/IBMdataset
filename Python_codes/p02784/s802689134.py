a,b=map(int, input().split()) 
c=list(map(int, input().split()))

if sum(c) >= a:
    print('Yes')
if sum(c) < a:
    print('No')