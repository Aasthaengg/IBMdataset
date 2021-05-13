s = input()
k = int(input())

target_ls = []
for start in range(len(s)):
    for length in range(1,k+1):
        target_ls.append(s[start:start + length])
unique_ls = list(set(target_ls))
unique_ls.sort()
print(unique_ls[k-1])
