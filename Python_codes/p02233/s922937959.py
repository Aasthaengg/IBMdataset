n = int(input())
def fib(x):
    lst=[1,1]
    for i in range(x-1):
        z = len(lst)
        y = int(lst[z-2])+int(lst[z-1])
        lst.append(y)
    print(lst[x])
fib(n)
