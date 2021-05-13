num=int(input())
val=0
for i in input().split():
  val+=int(i)
print("YES" if val%2==0 else "NO")