n = int(input())
for i in range(1,6):
    if n%(10*i) == 0:
        print(10)
        exit()
print(sum(list(map(int, str(n)))))