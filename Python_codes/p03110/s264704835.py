n = int(input())
output = 0
for i in range(n):
    x,u = map(str,input().split())
    if u == "JPY":
        output += int(x)
    else:
        output = output + 380000 * float(x)
print(output)