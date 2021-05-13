n=(int)(input())
a=[1]
for i in range(2, n):
  temp = i ** 2
  while(temp <= n):
    a.append(temp)
    temp *= i
a = sorted(set(a))
#print(a)
print(list(i for i in a if i <= n)[-1])