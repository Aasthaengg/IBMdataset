n = int(input())
a = int(input())
remain = n % 500
judge = remain <= a
result = "Yes" if judge else "No"
print(result)