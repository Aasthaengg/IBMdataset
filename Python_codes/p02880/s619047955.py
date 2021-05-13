n = int(input())
result = 'No'
for i in range(1,10):
    if n / i in [1,2,3,4,5,6,7,8,9]:
        result = 'Yes'
print(result)