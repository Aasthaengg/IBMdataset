a,b,c= input().split()
x,y,z=(int(a),int(b),int(c))
if x-y >= z:
    print(0)
else:
    ans = z-(x-y)
    print(ans)