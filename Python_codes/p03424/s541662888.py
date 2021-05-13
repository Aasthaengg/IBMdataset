n = int(input())
s = [x for x in input().split()]

count = 0
if 'P' in s:
    count += 1
if 'W' in s:
    count += 1
if 'G' in s:
    count += 1
if 'Y' in s:
    count += 1

print('Three' if count == 3 else 'Four')