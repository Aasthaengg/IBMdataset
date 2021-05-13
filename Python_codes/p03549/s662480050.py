n,m = map(int,input().split())
print(int((m*1900+(n-m)*100)/(0.5)**m))