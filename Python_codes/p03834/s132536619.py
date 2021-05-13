n=str(input())
for i in n:
    if i==",":
        n=n.replace(","," ")
print(n)