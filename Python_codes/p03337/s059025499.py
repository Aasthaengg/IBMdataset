a, b = map(int, input().split())

ansa= a+b
ansb= a-b
ansc= a*b
li = [ansa,ansb,ansc]

print(max(li))