h,w = map(int,input().split())
sharp = ["0"]*(w+2)
for i in range(w+2):
  sharp[i] = "#"

print("".join(sharp))
for j in range(h):
  a = list(input())
  a.append("#")
  a.insert(0,"#")
  print("".join(a))
print("".join(sharp))