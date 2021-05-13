n = int(input())
a = list(map(int,input().split()))
odd = 1
 
for a in a:
    if a % 2 == 0:
        odd *= 2
 
print(3**n - odd)