month, day = map(int, input().split())
print(month if month<=day else month-1)