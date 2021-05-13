A,B=[int(x) for x in input().split(" ")]
for i in range(20):
    if A+(i-1)*(A-1)>=B: break
print(i)