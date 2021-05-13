inp=list(map(int,input().split()))

if inp[0]*inp[1]>=inp[2]*inp[3]:
    print(inp[0]*inp[1])
else:
    print(inp[2]*inp[3])