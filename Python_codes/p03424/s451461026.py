from collections import Counter
N = input()
color_list = [i for i in input().split()]
result = len(Counter(color_list))

if result == 3:
    result = 'Three'
elif result == 4:
    result = 'Four'

print(result)