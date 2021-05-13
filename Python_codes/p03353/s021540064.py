s = input()
K = int(input())


substrings = set()
for i in range(len(s)):
    for j in range(1, K+1):
        substrings.add(s[i:i+j])

print(sorted(list(substrings))[K-1])
