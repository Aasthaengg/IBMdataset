n= list(input())
make = 0
for i in range(len(n)):
         if n[i] == "x":
                  make += 1
if make >= 8:
         print("NO")
else:
         print("YES")
