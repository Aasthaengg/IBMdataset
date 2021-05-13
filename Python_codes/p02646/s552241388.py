buf = list(map(int, input().split()))
A=buf[0]
V=buf[1]
buf2 = list(map(int, input().split()))
B=buf2[0]
W=buf2[1]
T= int(input())

if A>B:
  if B-W*T<A-V*T:
    print("NO")
  else:
    print("YES")
else:
  if B+W*T>A+V*T:
    print("NO")
  else:
    print("YES")  