a,b = map(int, input().split()) 
print(min(min(a,12)-1,min(max(b,a-1),31)-1)+1)