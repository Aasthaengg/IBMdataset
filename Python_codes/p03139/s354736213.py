a,b,c = [int(i) for i in input().split()]

print(min(b,c),b+c-a if b + c >= a else 0)