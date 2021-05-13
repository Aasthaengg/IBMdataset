n = int(input())
s = input()
count = 0
r = s.count('R')
g = s.count('G')
b = s.count('B')
for i in range(0,n-2):
    for j in range(i+1,n-1):
        if j < 2*j -i <= n-1 and sorted([s[i],s[j],s[2*j-i]]) == ['B','G','R']:
            count += 1
print(r*g*b - count)