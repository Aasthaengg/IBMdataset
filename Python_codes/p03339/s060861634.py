n = int(input())
s = list(input())

num_eas = s.count('E')


res = []
res += [num_eas - s[0].count("E")]

for i in range(1,n):
    res += [res[i-1] + s[i-1].count("W") - s[i].count("E")]
    
print(min(res))
