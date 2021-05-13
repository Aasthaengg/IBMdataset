import sys

keyword = input().lower()
count = 0
for line in sys.stdin:
    count += sum([1 for word in line.lower().split() if word == keyword])
    
print(count)