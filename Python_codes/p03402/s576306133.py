A,B = map(int,input().split())
A,B = A-1,B-1
print(100,100)

for n in range(50):
  print(50*"."+50*"#")
  a = min(24,A)
  b = min(24,B)
  print(b*".#"+(50-2*b)*"."+a*"#."+(50-2*a)*"#")
  A-=a
  B-=b