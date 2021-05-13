import sys

n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
    
for i in a:
    if i % 2 == 0:
        continue
    else:
        print("first")
        sys.exit()
        
print("second")