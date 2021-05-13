w,a,b = map(int,input().split())
print((a+w<b)*(b-a-w) or (b+w<a)*(a-b-w) or 0)