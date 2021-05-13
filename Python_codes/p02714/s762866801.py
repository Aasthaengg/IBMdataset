n = int(input())
s = input()
count = 0

fullcount= s.count('R')*s.count('G')*s.count('B')

for i in range(n-2):
    for j in range(i+1,n):
        k = 2*j-i
        if k > (n-1):
            break
        if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
            count += 1
ans = fullcount - count
print(ans)