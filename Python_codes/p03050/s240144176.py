n = int(input())
s = set()

for i in range(1,int(n**0.5)+1):
    if n//i == n%i:
        s.add(i)
    x = (n-i)//i
    if x and n//x == n%x:
        s.add(x)
print(sum(list(s)))

