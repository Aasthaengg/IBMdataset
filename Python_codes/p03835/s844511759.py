k,s = map(int, input().split())
count = 0
for x in range(k+1):
    for y in range(x, k+1):
        z=s-x-y
        if y <= z <= k:
            if x==y and y==z:
                count += 1
            elif x==y or y==z or z==x:
                count += 3
            else:
                count += 6
        
print(count)
print("\n")

