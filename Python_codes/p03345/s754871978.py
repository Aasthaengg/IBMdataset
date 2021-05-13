a,b,c,k = map(int, input().split())
print(0 if a==b else a-b if k%2==0 else b-a)