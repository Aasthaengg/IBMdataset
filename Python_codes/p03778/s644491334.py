w,a,b = map(int,input().split())
print(max(b-a-w,0) if a<=b+w else max(a-b-w,0))