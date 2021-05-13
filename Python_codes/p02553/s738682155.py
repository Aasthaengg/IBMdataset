a,b,c,d = map(int,input().strip().split())
print(max(a*c,max(a*d,max(b*c,b*d))))