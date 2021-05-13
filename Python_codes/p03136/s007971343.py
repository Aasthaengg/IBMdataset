n = int(input())
l = [int(s) for s in input().split()]

max_length = max(l)
print ('Yes') if max_length < sum(l) - max_length else print('No')