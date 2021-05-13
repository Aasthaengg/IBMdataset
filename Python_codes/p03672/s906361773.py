s=input()
n=len(s)
for i in reversed(range(n-1)):
    if i%2:
        l=s[:i//2+1]
        r=s[i//2+1:i+1]
        ok=True
        for j in range(i//2+1):
            if l[j]!=r[j]:
                ok=False
        if ok:
            print(i+1)
            exit()