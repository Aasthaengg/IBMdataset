def counter(s):
    return len(bin(s))-(bin(s).rfind("1")+1)

n = input()
a = input()
b = map(int,a.split(" "))
c = map(counter,b)
d = min(c)
print(d)