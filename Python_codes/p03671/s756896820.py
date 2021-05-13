rp=list(map(int,input().split()))
print(min([sum(rp)-x for x in rp]))
