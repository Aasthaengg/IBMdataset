a,b = map(int,input().split())

aa = a+a-1
bb = b+b-1
ab = a+b

lists = [aa,bb,ab]
print(max(lists))
