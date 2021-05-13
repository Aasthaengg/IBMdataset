h, w = [int(ip) for ip in input().split()]
y, x = [int(ip) for ip in input().split()]

count = w * h
delete = x * h + y * w
delete -= x * y

print(count - delete)