s = list(input())
a = [s.count('a'),s.count('b'),s.count('c')]
print("NO" if max(a)-min(a)>1 else "YES")