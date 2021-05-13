import sys
input = sys.stdin.readline
 
N = int(input().rstrip('\n'))
numbers = list(map(int,input().rstrip('\n').split()))

print(sum(numbers)-N)