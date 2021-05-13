n = int(input())
ns = []
max_profit = -1000000000
min_value = int(input())
for i in range(1,n):
    num = int(input())
    max_profit = max(max_profit, num-min_value)
    min_value = min(num, min_value)
print(max_profit)
    
