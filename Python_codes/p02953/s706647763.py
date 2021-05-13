N = int(input())
H = list(map(int,input().split()))
a = 0

for h in H:
  if h<a:
    print("No")
    exit()
  a = max(a,h-1)

print("Yes")