a,b = [int(_) for _ in input().split()]
a_str = str(b)*a
b_str = str(a)*b
list_str = [a_str,b_str]
list_str.sort()
print(list_str[0])
