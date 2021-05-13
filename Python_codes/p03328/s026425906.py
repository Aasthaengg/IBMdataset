a,b=map(int,input().split())
diff = b-a
tall = sum([i for i in range(1, diff+1)])
print(tall-b)