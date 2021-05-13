total = int(input())
until = int(input())
fee1 = int(input())
fee2 = int(input())

if total - until > 0:
    diff = total - until
    print(until * fee1 + diff * fee2)
else:
    print(total * fee1)