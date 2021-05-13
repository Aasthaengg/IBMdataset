
a, b, c = input().split()

list = [a, b, c]

print(len(list) if len(list)==len(set(list)) else len(set(list)) ) 