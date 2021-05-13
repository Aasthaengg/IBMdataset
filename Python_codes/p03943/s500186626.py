candys = [int(x) for x in input().split()]

output = 'No'
if(max(candys) == sum(candys)/2):
    output = 'Yes'
    
print(output)