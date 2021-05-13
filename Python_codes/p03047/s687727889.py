n, k = map(int,input().split() )
count = 0
for i in range(0,n+1):
    #print("ifの前","i+k=",i+k)
    if i + k <= n:
        count+=1
    else:
        pass
print(count)
