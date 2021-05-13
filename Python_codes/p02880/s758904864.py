n = int(input())
def f():
    for i in  range(1,10):
        for j in range(1,10):
            if i*j ==n:
                return "Yes"
    return "No"
print(f())
