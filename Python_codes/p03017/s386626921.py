n,a,b,c,d = map(int,input().split())
s = input()
if d<c:
    if "##" not in s[a-1:d] and '...' in s[b-2:d+1]:
        print('Yes')
    else:
        print('No')
    
else:
    if "##" not in s[a-1:d]:
        print('Yes')
    else:
        print('No')