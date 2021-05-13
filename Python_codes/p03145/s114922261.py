li = list(map(int,input().split()))
li.remove(max(li))
print(int(li[0] * li[1] / 2))