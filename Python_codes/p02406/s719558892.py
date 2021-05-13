n=input()
l=[]
for i in range(int(n)+1):
    if i%3==0:
        l.append(i)
    elif "3" in str(i):
        l.append(i)
print(" "+" ".join(map(str,l[1:])))