n = int(input())
list_a = [int(m) for m in input().split()]
for i in list_a:
    if i % 2 != 0:
        continue
    elif not (i % 3 == 0 or i % 5 == 0):
        print("DENIED")
        exit()
print("APPROVED")