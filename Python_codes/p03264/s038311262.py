K = int(input())    
count = 0
i = 0
j = 0

if K == 2:
    count = 1

elif K == 3:
    count = 2

elif K > 3:
    while i < K:
        i += 1
        j = i + 1

        while j <= K:
            
            count += 1
            
            j += 2
            
print(count)