tmp = list(map(lambda n : int(n), input().split(" ")))
tmp.sort(reverse=True)
 
print(tmp[0] - tmp[2])