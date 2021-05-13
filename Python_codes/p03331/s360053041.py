num = int(input())
if num % 10 == 0:
    ans = 10
else:   
    s = str(num)
    array = list(map(int, s))
    ans = sum(array)
print (ans)

