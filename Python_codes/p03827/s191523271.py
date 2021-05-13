N = int(input())
IorD = [1 if i == "I" else -1 for i in list(input())]
Max = 0
x = 0
for i in IorD:
    x += i
    if x>Max:
        Max = x
        
print(Max)
