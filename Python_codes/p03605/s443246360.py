def func(l):
    for i in l:
        if i == "9":
            return 1
    return 0

l=list(input())
print("Yes" if func(l)==1 else "No")