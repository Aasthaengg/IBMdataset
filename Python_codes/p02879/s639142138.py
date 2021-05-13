a,b= map(int, input().split())
#print(len(str(a)+str(b))) 
print(a*b if len(str(a)+str(b))<3 else -1)