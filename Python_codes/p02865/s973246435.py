n = int(input())
counter = 0

if n%2 == 0:
    half = n//2
else:
    half = (n-1)//2
for i in range(1, half+1):
    if i != n-i:
        counter +=1

print(counter)
