from collections import Counter
S = input()
work = sorted(list(Counter(S).values()), reverse=True)
a = work[0]
b = work[1] if len(work)>1 else 0
c = work[2] if len(work)>2 else 0
result = "YES"
if (a > b + 1 or a > c + 1):
    result = "NO"
print(result)