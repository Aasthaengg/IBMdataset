g = [31,28,31,30,31,30,31,31,30,31,30,31]
 
tmp = input().split(" ")
print("Yes") if g[int(tmp[0]) - 1] == g[int(tmp[1]) - 1] else print("No")