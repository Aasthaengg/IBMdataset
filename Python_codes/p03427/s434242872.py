n = [int(i) for i in list(input())]
l = len(n)

ans =  max((n[0]-1) + 9*(l-1),sum(n))
print(ans)