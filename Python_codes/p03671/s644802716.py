a,b,c=map(int,input().split())
numbers=[]
numbers.append(a)
numbers.append(b)
numbers.append(c)
numbers.remove(max(numbers))
print(sum(numbers))
