k=int(input())
s=input()
n=len(s)
print(s[:k]+'.'*(3 if n>k else 0))