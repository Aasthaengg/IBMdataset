ary = list(map(lambda n: int(n), input().split(" ")))
ary.sort()
 
print("Yes") if ary[0] + ary[1] == ary[2] else print("No")