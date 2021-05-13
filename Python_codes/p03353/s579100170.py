s = input()
K = int(input())
substring = []
# print(s, K)
for i in range(len(s)):
    for j in range(1, min(K+1, len(s)+1)):
        # print(s[i:i+j])
        substring.append(s[i:i+j])

substring = list(set(substring))
substring.sort()

# print(substring)
print(substring[K-1])