a,b=map(int,input().split())
all=[i*(i+1)//2 for i in range(1,1000)]
diff=b-a-1
print(all[diff]-b)