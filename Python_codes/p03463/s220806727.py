n,a,b = map(int,input().split())	
ans=[ "Alice", "Borys", "Draw"]
if (b-a) %2 ==0:
    print(ans[0])
else:
    print(ans[1])