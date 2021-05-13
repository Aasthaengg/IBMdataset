# solution
n, m = map(int, input().split())
strs = str(input())
count = 0
for i in range(n):
    if strs[i:i+2] == 'LL' or strs[i:i+2] == 'RR':
        count += 1
print(min((count + 2*m), n-1))