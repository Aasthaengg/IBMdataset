x,a,b = map(int,input().split())
print("AB"[int(abs(x-a)<=abs(x-b))-1])