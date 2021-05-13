input()
print(sum(map(lambda a:len(bin(int(a)&-int(a)))-3,input().split())))
