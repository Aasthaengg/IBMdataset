N = int(input())

nums = list(map(int,input().split(' ')))

count = 0
existOdd = True
while existOdd:
    for i in nums:
        if i%2!=0:
            existOdd = False
            break
    
    if existOdd:
        for i in range(N):
            nums[i] /= 2
        
        count+=1
    
print(count)
