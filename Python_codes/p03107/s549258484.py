s=input()
s=[i for i in s]
ans=min(s.count('0'),s.count('1'))
print(2*ans)