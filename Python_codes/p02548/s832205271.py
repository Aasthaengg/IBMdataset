n=int(input())
print(sum([n//a+(0 if n%a else -1) for a in range(1,n)]))
