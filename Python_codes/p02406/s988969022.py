n = int(input())
for i in range(n):
    if (i+1)%3 == 0 or "3" in str(i+1):
        print(" " + str(i+1), end='')
print()