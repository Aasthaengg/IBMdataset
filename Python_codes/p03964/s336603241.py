n = int(input())
e = [[int(i) for i in input().split()] for i in range(n)] 
a=e[0][0]
b=e[0][1]
for i in range(n-1):
  k=[-(-a//(e[i+1][0])),-(-b//(e[i+1][1]))]
  a=max(k)*(e[i+1][0])
  b=max(k)*(e[i+1][1])
print(a+b)