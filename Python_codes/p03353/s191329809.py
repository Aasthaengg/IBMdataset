
s = input()
n = len(s)
k = int(input())
substr = []
for j in range(1, k+1):
    for i in range(n-j+1):
        sub = s[i:i+j]
        if sub not in substr:
            substr.append(sub)
substr.sort()
print(substr[k-1])
