n = int(input())

if n < 100:
    result = "ABC"# + "00" + str(n)
elif n > 999:
    n = n - 999
    result = "ABD" #+ str(n)
else:
    result = "ABC" #+ str(n)

print(result)