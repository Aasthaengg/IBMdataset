a=int(input())
n=[i*111 for i in range(1,10)]
if a in n:
    print(a)
    exit()

n.append(a)
n=sorted(n)
print(n[n.index(a)+1])
