A,B,C=map(int,input().split(' '))
ans = 'Yes' if C-A>=0 and C-B<=0 else 'No'
print(ans)