n,a,b,c,d=map(int,input().split())
s=input()
print('YNeos'['##' in s[a-1:max(c,d)] or not(c<d or '...' in s[b-2:d+1])::2])