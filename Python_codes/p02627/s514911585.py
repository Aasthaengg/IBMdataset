def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())

s=input()
if s.isupper():
    print("A")
else:
    print("a")