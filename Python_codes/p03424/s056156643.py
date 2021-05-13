n = int(input())

l = len(set(list(map(str, input().split()))))

if l == 1:
    print("One")
elif l == 2:
    print("Two")
elif l == 3:
    print("Three")
else:
    print('Four')