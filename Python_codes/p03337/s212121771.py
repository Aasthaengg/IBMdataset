A,B = map(int,input().split())

res = [0]*3
res[0] = A+B
res[1] = A-B
res[2] = A*B

print(max(res))