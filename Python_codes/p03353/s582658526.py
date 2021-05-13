s = input()
K = int(input())
print(sorted(set(s[l:r+1] for l in range(len(s)) for r in range(l, min(l+K,len(s)))))[K-1])