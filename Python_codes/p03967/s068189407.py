s=input()
n=len(s)

plst=[1 if c=='p' else 0 for c in s]
p=sum(plst)

print(n//2-p)