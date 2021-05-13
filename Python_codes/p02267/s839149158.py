n = int(input())
s = input().split()
n = int(input())
t = input().split()
count = 0
for a in t:
    if a in s:
        count += 1
        
print(count)