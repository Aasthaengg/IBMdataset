from collections import Counter
s = input()
ans = len(s)*(len(s)+1)//2
s = Counter(s)

for _, val in s.items():
    ans -= val*(val+1)//2

ans += 1
print(ans)
