total_number = int(input())
number = list(map(int, input().split()))
for value in number:
    if value % 2 == 0 and (value % 3 != 0 and value % 5 != 0):
        print("DENIED")
        quit()
print("APPROVED")