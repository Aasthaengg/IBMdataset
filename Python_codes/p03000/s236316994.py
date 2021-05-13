n, x = map(int, input().split())
l = list(map(int, input().split()))
result = 0
res = 0
for i in l:
    res+=1
    result += i
    if(result > x):
        break
else:
    res+=1
    
    
print(res)