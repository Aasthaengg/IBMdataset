n=list(input())
a=True
for i in range(len(n)//2):
    if n[i]!=n[len(n)-1-i]:
        a=False
        break
print('Yes' if a else 'No')