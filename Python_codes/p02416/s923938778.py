'''
Input   Output
123     6
55      10
1000    1
0
'''
for str in iter(input, "0"):
 print(sum([int(c) for c in str]))