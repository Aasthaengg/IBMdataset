s = input()
k = int(input())
a =[chr(ord('a') + i) for i in range(26)]

tar = set()
alpha_idx = 0
while len(tar) < k:
    alpha = a[alpha_idx]
    for i in range(len(s)):
        if s[i] == alpha:
            for j in range(i+1, min(len(s)+1,i+1+k)):
                tar.add(s[i:j])
    alpha_idx += 1
tar = list(tar)
tar.sort()
print(tar[k-1])

