a,b =map(int,input().split())
print(b*((b-1)**(a-1)) if a>1 else b)