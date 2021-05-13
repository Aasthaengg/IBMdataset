s = 'acababaababa'
a,b = map(int,input().split())
print('Yes' if s[a-1] ==s[b-1]  else 'No')