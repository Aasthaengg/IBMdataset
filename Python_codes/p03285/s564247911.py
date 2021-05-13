n=int(input())
l=[n]
while n>6:
    n=n-7
    l.append(n)
print('Yes' if any([l[j]%4==0 for j in range(len(l))]) else 'No')