n = int(input())

vac = []
firstDay = list(map(int, input().split()))

for _ in range(n-1):
    newTotal = [0,0,0]
    
    secondDay = list(map(int, input().split()))
    for j, second in enumerate(secondDay):
        temp = 0
        for i, first in enumerate(firstDay):
            if i != j:
                temp = max(temp, first + second)
                
        newTotal[j] = temp   
                    
    firstDay = newTotal
    
print(max(firstDay))