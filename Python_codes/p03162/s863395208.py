n = int(input())

aa = 0
bb = 0
cc = 0 

for i in range(n):
    a,b,c = map(int,input().split())
    aa,bb,cc = max(bb + a, cc + a),max(aa + b, cc + b),max(aa + c, bb + c)

print(max(aa,bb,cc))