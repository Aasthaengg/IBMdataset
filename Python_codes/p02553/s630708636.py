x = [int(i) for i in input().split(" ")]
ans = max([x[0]*x[2],x[0]*x[3],x[1]*x[2],x[1]*x[3]])

print(ans)