n=input()
l=len(n)
m=1000000000000000
for i in range(l-2):
    m=min(m,abs(753-int(n[i:i+3])))
print(m)
