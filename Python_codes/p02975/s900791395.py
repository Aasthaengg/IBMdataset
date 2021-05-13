from collections import Counter

n=int(input())
*a,=map(int,input().split())

cnt=sorted(list(Counter(a).items()),key=lambda x:x[0])

if len(cnt)==1 and cnt[0][0]==0:
    print('Yes')
elif n%3==0 and len(cnt)==2 and cnt[0][0]==0 and cnt[0][1]==n//3:
    print('Yes')
elif n%3==0 and len(cnt)==3 and cnt[0][0]^cnt[1][0]^cnt[2][0]==0 and cnt[0][1]==n//3 and cnt[1][1]==n//3 and cnt[2][1]==n//3:
    print('Yes')
else:
    print('No')
