a,b,c = map(int,input().split())
print("Yes" if (a+b+c) / max(a,b,c)==2 else "No")