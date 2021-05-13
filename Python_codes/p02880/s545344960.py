A = int(input()) 
ans = min([A//i for i in range(1,10) if A%i == 0], default = 0)

print("Yes") if 1<=ans<=9 else print("No")