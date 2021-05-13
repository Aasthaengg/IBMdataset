inp=list(input().split())
ans=0
if inp[1]=="+":
    ans=int(inp[0])+int(inp[2])
else:
    ans=int(inp[0])-int(inp[2])
print(ans)