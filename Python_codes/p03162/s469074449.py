import sys
from collections import deque
input = sys.stdin.readline
number=int(input())
vacation = [list(map(int,input().rstrip().split())) for _ in range(number)]
#print(vacation)
#capable = deque([0,1,2])
#did = deque([])
#print(max(vacation[0]))
table = [[0]*3 for _ in range(number+1)]
for i in range(1,number+1):
    table[i][0] = max(table[i-1][1],table[i-1][2]) + vacation[i-1][0]
    table[i][1] = max(table[i-1][0],table[i-1][2]) + vacation[i-1][1]
    table[i][2] = max(table[i-1][0],table[i-1][1]) + vacation[i-1][2]
print(max(table[number]))
