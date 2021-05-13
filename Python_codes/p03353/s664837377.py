s = input()
k = int(input())

substring = []
len_s = len(s)
for length in range(1, k+1):
    for i in range(len_s-length+1):
        substring.append(s[i:i+length])

substring = sorted(list(set(substring)))
print(substring[k-1])
